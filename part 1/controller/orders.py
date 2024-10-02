from flask import request, jsonify
import pymysql
from datetime import datetime
import db


def add_orders():
    
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    order_data=request.get_json()
    orderuser_id=order_data['user_id']
    order_status=order_data['status']
    
    mycursor.execute(
        """
        INSERT INTO orders (user_id,status)
        VALUES (%s,%s)
        """, 
        (orderuser_id,order_status)
    )
    
    order_id=mycursor.lastrowid
    db_conn.commit()
    mycursor = db_conn.cursor()
    
    
    orderproduct_id = order_data['orderproduct_id']
    order_quantity = order_data['quantity']
    order_unitprice = order_data['unit_price']

    mycursor.execute(
        """
        INSERT INTO order_details (order_id, product_id, quantity, unit_price)
        VALUES (%s, %s, %s, %s)
        """, 
        (order_id, orderproduct_id, order_quantity, order_unitprice)
    )

    db_conn.commit()
    return f"the order was succefully added"

    

def get_orders():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    fname=request.args.get('first_name')
    lname=request.args.get('last_name')
    date=request.args.get('order_date')
    product=request.args.get('product_name')
    
    query="""
        SELECT orders.*, CONCAT(users.first_name, ' ', users.last_name) as customer_name, products.product_name as product_name 
        FROM orders
        JOIN users ON orders.user_id = users.user_id
        JOIN order_details ON orders.order_id = order_details.order_id
        JOIN products ON order_details.product_id = products.product_id
    """
    
    query_condition=[]
    query_param=[]
    
    if fname:
        query_condition.append("users.first_name = %s")
        query_param.append(fname)
     
    if lname:
        query_condition.append("users.last_name = %s")
        query_param.append(lname)
    
    if date:
        query_condition.append("orders.order_date = %s")
        query_param.append(date)
        
    if product:
        query_condition.append("products.product_name = %s")
        query_param.append(product)
        
    if query_condition:
        query+= ' WHERE ' + ' AND '.join(query_condition)
        
        
    mycursor.execute(query,query_param)
    
    orders=mycursor.fetchall()
    
    return jsonify(orders) 