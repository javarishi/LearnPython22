import learn_day014.ConnectionUtil as util

conn = util.get_connection()
db_cursor = conn.cursor()

query = "UPDATE actor SET first_name = %s , last_name= %s WHERE actor_id = %s"
val = ('CARL', 'DANVERS', 252)

db_cursor.execute(query, val)
conn.commit()
result= db_cursor.rowcount
print("Number of records inserted ", result)

util.close_connection(conn)