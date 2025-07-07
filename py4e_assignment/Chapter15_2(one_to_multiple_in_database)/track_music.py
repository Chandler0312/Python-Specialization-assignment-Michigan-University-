import sqlite3
conn = sqlite3.connect('music_database.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Track(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);

CREATE TABLE Album(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Genre(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    genre TEXT UNIQUE
);
            
CREATE TABLE Artist(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist TEXT UNIQUE);
''')

with open('tracks.csv','r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        pieces = line.split(',')
        if len(pieces) != 7:
            continue
        track_title = pieces[0]
        artist_name = pieces[1]
        album_title = pieces[2]
        track_len = pieces[3]
        track_rating = pieces[4] 
        track_count = pieces[5]
        genre = pieces[6]

        cur.execute("INSERT OR IGNORE INTO Artist (artist) VALUES (?)" , (artist_name,))
        cur.execute("SELECT id FROM Artist WHERE artist = ?", (artist_name,))
        artist_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Album (artist_id,title) VALUES(?,?)" , (artist_id,album_title))
        cur.execute("SELECT id FROM Album WHERE title = ? ",(album_title,))
        album_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Genre (genre) VALUES(?)" , (genre,))
        cur.execute("SELECT id FROM Genre WHERE genre = ?" , (genre,))
        genre_id = cur.fetchone()[0]

        cur.execute('''
            INSERT OR REPLACE INTO Track
            (title,album_id,genre_id,len,rating,count) 
            VALUES (?,?,?,?,?,?)
        ''',(track_title,album_id,genre_id,track_len,track_rating,track_count,))

conn.commit()
conn.close()
print("We've create the database successfully and filled in the data")