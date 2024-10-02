from flask import request, jsonify
import pymysql
from datetime import datetime
import db

def pending_payments():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""
    SELECT SUM(amount) AS pending_payments
    FROM payments
    WHERE status = 'Pending'

        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  AND payment_date BETWEEN '2024-09-01' AND %s ; "
        query_params.append(start_date)
        query_params.append(end_date)
        mycursor.execute(query,query_params)
        total_rev=mycursor.fetchall()
        return jsonify(total_rev),200
    else:
        if start_date:
            query+="  AND payment_date >= %s"
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND payment_date <= %s"
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
            
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200


def successful_payments():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""
    SELECT SUM(amount) AS successful_payments
    FROM payments
    WHERE status = 'Completed'
 
        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  AND payment_date BETWEEN %s AND %s "
        query_params.append(start_date)
        query_params.append(end_date)
        mycursor.execute(query,query_params)
        total_rev=mycursor.fetchall()
        return jsonify(total_rev),200
    else:
        if start_date:
            query+="  AND payment_date >= %s"
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND payment_date <= %s"
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
            
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200
