from flask import request, jsonify
import pymysql
from datetime import datetime
import db





def top_cities_by_sales():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT U.city, COUNT(O.order_id) AS total_orders
        FROM users U
        JOIN orders O ON U.user_id = O.user_id
        GROUP BY U.city
        ORDER BY total_orders DESC
        LIMIT 5;

        """
    )
    result=mycursor.fetchall()
    return jsonify(result),200

def top_countries_by_sales():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    mycursor.execute("""
        SELECT U.country, SUM(PY.amount) AS total_revenue
        FROM users U
        JOIN orders O ON U.user_id = O.user_id
        JOIN payments PY ON O.order_id = PY.order_id
        WHERE PY.status = 'Completed'
        GROUP BY U.country
        ORDER BY total_revenue DESC;

        """
    )
    result=mycursor.fetchall()
    return jsonify(result),200