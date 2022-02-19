import learn_day014.ConnectionUtil as util

conn = util.get_connection()
db_cursor = conn.cursor()

query = "DELETE FROM ACTOR WHERE actor_id = %s"
val = (252,)

db_cursor.execute(query, val)
conn.commit()
result= db_cursor.rowcount
print("Number of records DELETED ", result)

util.close_connection(conn)