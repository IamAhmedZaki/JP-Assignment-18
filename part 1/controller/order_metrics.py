from flask import request, jsonify
import pymysql
from datetime import datetime
import db




def total_orders():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""SELECT COUNT(*) AS total_orders
FROM orders


        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  WHERE order_date BETWEEN %s AND %s "
        query_params.append(start_date)
        query_params.append(end_date)
        mycursor.execute(query,query_params)
        total_rev=mycursor.fetchall()
        return jsonify(total_rev),200
    else:
        if start_date:
            query+="  WHERE order_date >= %s"
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  WHERE order_date <= %s"
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
            
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200

def pending_orders():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""
    SELECT COUNT(*) AS pending_orders
    FROM orders
    WHERE status = 'Pending'

        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  AND order_date BETWEEN %s AND %s "
        query_params.append(start_date)
        query_params.append(end_date)
        mycursor.execute(query,query_params)
        total_rev=mycursor.fetchall()
        return jsonify(total_rev),200
    else:
        if start_date:
            query+="  AND order_date >= %s"
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND order_date <= %s"
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
            
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200

    

def cancelled_orders():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""
    SELECT COUNT(*) AS cancelled_orders
    FROM orders
    WHERE status = 'Cancelled'

        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  AND order_date BETWEEN %s AND %s "
        query_params.append(start_date)
        query_params.append(end_date)
        mycursor.execute(query,query_params)
        total_rev=mycursor.fetchall()
        return jsonify(total_rev),200
    else:
        if start_date:
            query+="  AND order_date >= %s"
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND order_date <= %s"
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
            
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200


def successful_orders():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""
    SELECT COUNT(*) AS successful_orders
    FROM orders
    WHERE status IN ('Shipped', 'Delivered')

        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  AND order_date BETWEEN %s AND %s "
        query_params.append(start_date)
        query_params.append(end_date)
        mycursor.execute(query,query_params)
        total_rev=mycursor.fetchall()
        return jsonify(total_rev),200
    else:
        if start_date:
            query+="  AND order_date >= %s"
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND order_date <= %s"
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
            
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200
