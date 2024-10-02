import pymysql
from datetime import datetime
from flask import request,jsonify
import db

def add_product():
    
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    product_data=request.get_json()
    
    product_name=product_data['product_name']
    product__cat_i=product_data['category_id']#can this be automated??
    product_price=product_data['price']
    product_stock_quantity=product_data['stock_quantity']
    
    mycursor.execute(
        """
        INSERT INTO products (product_name, price, stock_quantity, category_id)
        VALUES (%s, %s, %s,%s)
        """, 
        (product_name,product_price,product_stock_quantity, product__cat_i)
    )
    
    db_conn.commit() 
    return f"product {product_name} successfully added"

def get_products():
    
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()

    category=request.args.get('category')
    
    
    if category:
        mycursor.execute("""
           SELECT products.*, categories.category_name as category_name 
            FROM products 
            JOIN categories ON products.category_id = categories.category_id 
            WHERE categories.category_name = %s
        """, (category,))
    else:
        mycursor.execute("""
            SELECT products.*, categories.category_name as category_name 
            FROM products 
            JOIN categories ON products.category_id = categories.category_id
        """)
    
    products = mycursor.fetchall()
    
    
    return jsonify(products), 200

