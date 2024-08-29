import mysql.connector

__cnx = None

def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(user='root', password='12345678', database='products')
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise
    return __cnx
