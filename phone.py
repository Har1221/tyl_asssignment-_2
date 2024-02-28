import sqlite3

conn = sqlite3.connect('numbers.db')

c = conn.cursor()

#c.execute("""CREATE TABLE numbers (
#          name text,
#          id integer,
#          phone integer,
#         email text
#)""")

#c.execute("INSERT INTO numbers VALUES ('zara',001,1234567890,'alex@gmail.com')")
#c.execute("INSERT INTO numbers VALUES ('avyuktha',001,9876543210,'bob@gmail.com')")
#c.execute("INSERT INTO numbers VALUES ('jhon',001,1357924680,'clara@gmail.com')")
#c.execute("INSERT INTO numbers VALUES ('ravi',001,2468013579,'daniel@gmail.com')")
#c.execute("INSERT INTO numbers VALUES ('gopal',001,1029384756,'clara@gmail.com')")

conn.commit()

c.execute("SELECT * FROM numbers WHERE id=001")

print(c.fetchall())

conn.commit()

conn.close()