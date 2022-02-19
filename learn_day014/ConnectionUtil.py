import mysql.connector as conn

def get_connection():
    db_conn = conn.connect(
        host="localhost",
        user="root",
        password="password",
        database = "sakila"
    )
    return db_conn

def close_connection(conn):
    conn.close()
    

