import sqlite3

# 连接到数据库（或创建新数据库）
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# 创建规范化的数据库表（包含Genre表）
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# 读取CSV文件并填充数据
with open('tracks.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # 跳过空行
        
        # 按逗号分割字段（注意处理带逗号的标题可能需要更复杂的解析，这里假设数据正确）
        parts = line.split(',')
        if len(parts) < 7:  # 确保包含所有必要字段
            continue
        
        track_title, artist_name, album_title, track_len, track_rating, track_count, genre_name = parts[:7]
        
        # 处理数值字段（转换为整数）
        try:
            track_len = int(track_len)
            track_rating = int(track_rating)
            track_count = int(track_count)
        except ValueError:
            continue  # 跳过无法转换的行
        
        # 插入或忽略Artist表（确保唯一性）
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_name,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
        artist_id = cur.fetchone()[0]
        
        # 插入或忽略Genre表（确保唯一性）
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre_name,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
        genre_id = cur.fetchone()[0]
        
        # 插入或忽略Album表（确保唯一性，关联Artist）
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album_title, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
        album_id = cur.fetchone()[0]
        
        # 插入或替换Track表（处理重复数据）
        cur.execute('''
            INSERT OR REPLACE INTO Track 
            (title, album_id, genre_id, len, rating, count) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (track_title, album_id, genre_id, track_len, track_rating, track_count))

# 提交事务并关闭连接
conn.commit()
conn.close()

print("数据库已成功创建并填充数据（music.db）")