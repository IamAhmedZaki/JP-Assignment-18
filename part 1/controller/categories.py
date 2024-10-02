import pymysql
from datetime import datetime
from flask import request
import db

def add_categories():
    db_conn=db.mysqlconnect()
    data=request.get_json()
    category_name=data['category_name']
    mycusor=db_conn.cursor()
    mycusor.execute("""
        INSERT INTO categories (category_name)
        VALUES (%s)
        """, 
        (category_name))
    db_conn.commit()
    return data
     
def all_categories():
    db_conn=db.mysqlconnect()
    
    mycusor=db_conn.cursor()
    mycusor.execute("""
        SELECT * from categories
        """)
    
    result=mycusor.fetchall()
    db_conn.commit()
    return result
    
