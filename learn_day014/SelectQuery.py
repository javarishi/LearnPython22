import learn_day014.ConnectionUtil as util

conn = util.get_connection()
db_cursor = conn.cursor()

select_query = "SELECT * FROM ACTOR WHERE ACTOR_ID > {} "
query_string = select_query.format('200')

db_cursor.execute(query_string)
result = db_cursor.fetchmany(10)

for eachRow in result:
    print(eachRow[0:3])

util.close_connection(conn)