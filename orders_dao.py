import mysql.connector
from sql_connection import get_sql_connection

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT id, product_id, quantity, order_date FROM orders")
    cursor.execute(query)
    response = []
    for (id, product_id, quantity, order_date) in cursor:
        response.append({
            'id': id,
            'product_id': product_id,
            'quantity': quantity,
            'order_date': order_date
        })
    return response

def insert_new_order(connection, order):
    cursor = connection.cursor()
    query = ("INSERT INTO orders (product_id, quantity) VALUES (%s, %s)")
    data = (order['product_id'], order['quantity'])

    try:
        cursor.execute(query, data)
        connection.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
        return None

def delete_order(connection, order_id):
    cursor = connection.cursor()
    query = ("DELETE FROM orders WHERE id = %s")
    try:
        cursor.execute(query, (order_id,))
        connection.commit()
        return cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
        return 0

if __name__ == '__main__':
    connection = get_sql_connection()
    orders = get_all_orders(connection)
    print("All Orders:", orders)
    new_order_id = insert_new_order(connection, {
        'product_id': 1,
        'quantity': 10
    })
    print(f"Inserted new order with ID: {new_order_id}")
