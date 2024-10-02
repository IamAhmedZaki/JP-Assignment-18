from flask import Flask,make_response,request
import db

from helper_functions import check_missing_fields
from queries.auth_queries import registration_checking
from queries.auth_queries import create_user
from queries.auth_queries import check_user
from helper_functions import hash_password

def signup():
    db_conn=db.mysqlconnection()
    fields=["username","email","password"]
    if request.is_json:
        body=request.get_json()
        if body is None or not body:
            return "please add a body "
        username=body.get('username')
        email=body.get('email')
        password=body.get('password')
        missing_field=check_missing_fields(fields,body)
        
        if missing_field:
            return f"please fill the required fields {','.join(missing_field)}"
        
        user_id=registration_checking(db_conn,username,email)
        
        if user_id:
            return "username and name registered already"
        
        hash=hash_password(password)
        
        user_creation=create_user(db_conn,username,email,hash)
        return f"user {username} created successfully"
    else:
        return 'email, password and username are required'
        
        
def login():
    db_conn=db.mysqlconnection()
    fields=['username','password']
    if request.is_json:
        body=request.get_json()
        if body is None or not body:
            return "please add a body "
        username=body.get('username')
        
        password=body.get('password')
        missing_fields=check_missing_fields(fields,body)
        
        if missing_fields:
            return f"please fill the missing fields{','.join(missing_fields)}"
        
        user_is=check_user(db_conn,username,password)
        if user_is:
            print("user found")
            
            res=make_response("user logged in")
            res.set_cookie(
                'user_id',
                str(user_is),
                httponly=True,  
                max_age=3600,       
                path='/',            
                samesite='Lax' 
            )
            return res
        
        else :
            res = make_response("user not found")
            res.set_cookie("user_id", "", expires=0, path="/")
            return res
        
def logout():
    res=make_response("logged out successfully")
    res.set_cookie("user_id","",expires=0, path="/")
    return res