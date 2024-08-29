from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import json

import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

# Initialize the database connection
connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    try:
        response = uom_dao.get_uoms(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        response = products_dao.get_all_products(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        request_payload = json.loads(request.form['data'])
        product_id = products_dao.insert_new_product(connection, request_payload)
        response = jsonify({'product_id': product_id})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    try:
        response = orders_dao.get_all_orders(connection)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:
        request_payload = json.loads(request.form['data'])
        order_id = orders_dao.insert_new_order(connection, request_payload)
        response = jsonify({'order_id': order_id})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        product_id = request.form.get('product_id')
        if product_id is None:
            return jsonify({'error': 'product_id is required'}), 400

        return_id = products_dao.delete_product(connection, product_id)
        response = jsonify({'product_id': return_id})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000, debug=True)
