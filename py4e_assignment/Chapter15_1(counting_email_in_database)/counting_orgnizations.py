import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filename = input("plz enter the filename:")
if len(filename) < 1:
    filename = 'mbox.txt'
filehandle = open(filename)
for lines in filehandle:
    if not lines.startswith("From "):
        continue
    else:
        fragment = lines.split()
        email = fragment[1]
        org = email.split('@')[1]                    
        # the variable name 'org' should be the same as follow
        cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
        row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
    conn.commit()                     
    # don't forget to use the method commit to write the data down into the db

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]),(row[1]))

cur.close()
# don't forget to use the close method at last




