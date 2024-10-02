from flask import request, jsonify
import pymysql
from datetime import datetime
import db





def total_revenue():
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    
    
    
    
    query="""SELECT SUM(amount) AS total_revenue
        FROM payments
        WHERE status = 'Completed'
        """
    
    
    query_params=[]
    
    if start_date and end_date:
        query+="  AND payment_date BETWEEN %s AND %s"
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
        
        
    
    

def revenue_by_product():
    
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    query="""
        SELECT 
            P.product_name, 
            SUM(OD.quantity * OD.unit_price) AS revenue
        FROM 
            Order_Details OD
        JOIN 
            Products P ON OD.product_id = P.product_id
        JOIN 
            Orders O ON OD.order_id = O.order_id
        JOIN 
            Payments PY ON O.order_id = PY.order_id
        WHERE 
            PY.status = 'Completed'
        """
    query_params=[]
    if start_date and end_date:
        query_params.append(start_date)
        query_params.append(end_date)
        query+=" AND O.order_date BETWEEN %s AND %s "
        mycursor.execute(query,query_params)
        result=mycursor.fetchall
        return jsonify(result),200
    else:
        if start_date:
            query+="  AND O.order_date >= %s"
            query+=""" 
            GROUP BY 
                P.product_name
            ORDER BY 
                revenue DESC;
            
             """ 
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND O.order_date <= %s "
            query+=""" 
            GROUP BY 
                P.product_name
            ORDER BY 
                revenue DESC;
            
             """ 
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
    query+=""" 
    GROUP BY 
        P.product_name
    ORDER BY 
        revenue DESC;
            
             """        
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200
        

            
    

def top_selling_products():
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    query="""
    SELECT 
    P.product_name, 
    SUM(OD.quantity) AS total_units_sold
    FROM 
    order_details OD
    JOIN 
    products P ON OD.product_id = P.product_id
    JOIN 
    orders O ON OD.order_id = O.order_id
        """
    query_params=[]
    if start_date and end_date:
        query_params.append(start_date)
        query_params.append(end_date)
        query+=" WHERE O.order_date BETWEEN %s AND %s "
        mycursor.execute(query,query_params)
        result=mycursor.fetchall
        return jsonify(result),200
    else:
        if start_date:
            query+="  WHERE O.order_date >= %s"
            query+=""" 
            GROUP BY 
                P.product_name
            ORDER BY 
                total_units_sold DESC
            LIMIT 5;
            
             """ 
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  WHERE O.order_date <= %s "
            query+=""" 
            GROUP BY 
                P.product_name
            ORDER BY 
                total_units_sold DESC
            LIMIT 5;
             """ 
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
    query+=""" 
    GROUP BY 
        P.product_name
    ORDER BY 
        total_units_sold DESC
    LIMIT 5;        
             """        
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200
 

def revenue_city():
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    db_conn=db.mysqlconnect()
    mycursor=db_conn.cursor()
    query="""
    SELECT 
    U.city, 
    SUM(PY.amount) AS total_revenue
    FROM 
    users U
    JOIN 
    orders O ON U.user_id = O.user_id
    JOIN 
    payments PY ON O.order_id = PY.order_id
    WHERE 
    PY.status = 'Completed'
        """
    query_params=[]
    if start_date and end_date:
        query_params.append(start_date)
        query_params.append(end_date)
        query+=" AND PY.payment_date BETWEEN %s AND %s "
        mycursor.execute(query,query_params)
        result=mycursor.fetchall
        return jsonify(result),200
    else:
        if start_date:
            query+="  AND PY.payment_date >= %s"
            query+=""" 
            GROUP BY 
                U.city
            ORDER BY 
                total_revenue DESC;
            
             """ 
        
            
            mycursor.execute(query,start_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
        
        if end_date:
            query+="  AND PY.payment_date <= %s "
            query+=""" 
            GROUP BY 
                U.city
            ORDER BY 
                total_revenue DESC;
            
             """ 
        
            
            mycursor.execute(query,end_date)
            total_rev=mycursor.fetchall()
            return jsonify(total_rev),200
    query+=""" 
    GROUP BY 
        U.city
    ORDER BY 
        total_revenue DESC;
            
             """        
    mycursor.execute(query)
    tot=mycursor.fetchall()
    return jsonify(tot),200
