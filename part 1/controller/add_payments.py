from flask import request
import pymysql
from datetime import datetime
import db

def add_payments():
    
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    payment_data=request.get_json()
    paymentorder_id=payment_data['order id']
    payment_amount=payment_data['amount']
    payment_status=payment_data['status']
    mycursor.execute(
        """
        INSERT INTO payments (order_id,amount,status)
        VALUES (%s,%s,%s)
        """, 
        (paymentorder_id,payment_amount,payment_status)
    )
    
    db_conn.commit()
