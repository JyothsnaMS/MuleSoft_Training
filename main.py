import sqlite3

conn = sqlite3.connect('movies_assignment.db')
c = conn.cursor()

# create a table
c.execute(""" CREATE TABLE movies_assignment (
            movie_name text,
            actor_name text,
            actress_name text,
            year_of_releases text,
            Genre text)
""")

# insert 1 record to table
c.execute("""INSERT INTO Movies values(
            'The Lost City',
            'Channing Tatum',
            'Sandra Bullocks',
            '2022',
            'Adventure')
            """)

# insert many records to table
movies_list = [('Red Notice', 'Rock', 'Gal Gadot', '2021', 'Action'),
              ('Barely Lethal', 'Samuel Jackson', 'Hailee Steinfield', '2015', 'Action'),
              ('I Care A Lot', 'Peter Dinklage', 'Rosamund Pike', '2020', 'Comedy')]

c.executemany("INSERT INTO Movies values(?,?,?,?,?)", movies_list)

# selecting all rows from Movies table
c.execute("SELECT * FROM Movies")
print(c.fetchall())

# selecting particular rows from Movies table
c.execute("SELECT * FROM MOVIES WHERE ACTOR_NAME = 'Rock'")
print(c.fetchall())

# commit a command
conn.commit()

# close the connection
conn.close()