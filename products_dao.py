import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT id, name, price, unit FROM products")
    cursor.execute(query)
    response = []
    for (id, name, price, unit) in cursor:
        response.append({
            'id': id,
            'name': name,
            'price': price,
            'unit': unit
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (name, price, unit) VALUES (%s, %s, %s)")
    data = (product['name'], product['price'], product['unit'])

    try:
        cursor.execute(query, data)
        connection.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
        return None

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE id = %s")
    try:
        cursor.execute(query, (product_id,))
        connection.commit()
        return cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
        return 0

if __name__ == '__main__':
    connection = get_sql_connection()
    product_id = insert_new_product(connection, {
        'name': 'Apples',
        'price': 5.00,
        'unit': 'kg'
    })
    print(f"Inserted product with ID: {product_id}")
