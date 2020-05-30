import sqlite3
#connect to sqlite3 and create a new database name it as 'emaildb.sqlite'
conn = sqlite3.connect('emaildb.sqlite')
#set a cursor or a pointer
cur = conn.cursor()
#if Counts table already exist then drop or delete that table
cur.execute('DROP TABLE IF EXISTS Counts')
#create a new Counts table with column email and count.Since it has two lines of command enclosed with '''
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#inbox.txt has text from https://www.py4e.com/code3/mbox-short.txt
fh = open('inbox.txt','r')
#extract email address
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
