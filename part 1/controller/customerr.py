from flask import request
import pymysql
from datetime import datetime
import db

def add_customerr():
    
    db_conn=db.mysqlconnect
    mycursor=db_conn.cursor()
    customer_data=request.get_json()
    customer_fname=customer_data['first_name']
    customer_lname=customer_data['last_name']
    customer_email=customer_data['email']
    customer_password=customer_data['password']
    customer_address=customer_data['address']
    customer_city=customer_data['city']
    customer_state=customer_data['state']
    customer_zipcode=customer_data['zipcode']
    customer_country=customer_data['country']
    customer_phone=customer_data['phone']
    
    
    
    mycursor.execute(
        """
        INSERT INTO users (first_name,last_name,email,passwords,address,city,state,zip_code,country,phone)
        VALUES (%s, %s, %s,%s,%s,%s,%s, %s, %s,%s)
        """, 
        (customer_fname,customer_lname,customer_email,customer_password,customer_address,customer_city,customer_state,customer_zipcode,customer_country,customer_phone)
    )
    
    db_conn.commit() 
    return f"Customer {customer_fname} {customer_lname} info was succefully added"


def get_customerr():
    db_conn=db.mysqlconnect()
    
    mycusor=db_conn.cursor()
    mycusor.execute("""
        SELECT * from users
        """)
    
    result=mycusor.fetchall()
    db_conn.commit()
    return result