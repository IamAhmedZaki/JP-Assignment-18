from flask import request, jsonify
import pymysql
from datetime import datetime
import db





def inventory_levels():
    
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT product_name, stock_quantity
        FROM products
        ORDER BY stock_quantity ASC;

        """
    )
    
    result=mycursor.fetchall()
    return jsonify(result),200

def out_of_stock_products():
    
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT product_name
        FROM products
        WHERE stock_quantity = 0;

        """
    )
    result=mycursor.fetchall()
    return jsonify(result),200
