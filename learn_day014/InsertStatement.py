import learn_day014.ConnectionUtil as util

conn = util.get_connection()
db_cursor = conn.cursor()

query = "INSERT INTO actor (first_name,last_name,last_update) VALUES (%s, %s, CURRENT_TIMESTAMP)"
val = [('KARA', 'DANVERS'),
       ('BERRY', 'ALAN'),
       ('OLIVER', 'QUEEN'),
       ('ALEX', 'DANVERS')
       ]

db_cursor.executemany(query, val)
conn.commit()
result= db_cursor.rowcount
print("Number of records inserted ", result)

util.close_connection(conn)