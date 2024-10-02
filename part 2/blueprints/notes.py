from flask import Flask,make_response,request
import db

from helper_functions import check_missing_fields
from queries.notes_queries import checkuser_exists
from queries.notes_queries import category_exists
from queries.notes_queries import create_note_query
from queries.notes_queries import is_notes_exists
from queries.notes_queries import update_notes_query
from queries.notes_queries import delete_notes_query
from queries.notes_queries import get_all_notes_query




def create_note():
    db_conn=db.mysqlconnection()
    
    if request.cookies.get("user_id") is None:
        return "Please Login"
    if request.is_json:
        fields=["Title","Content"]
        body=request.get_json()
        title=body.get("Title")
        content=body.get("Content")
        cat_id=body.get("category_id")
        missiing_fields=check_missing_fields(fields,body)
        user_id=request.cookies.get("user_id")
        user=checkuser_exists(db_conn,int(user_id))
        
        if missiing_fields:
            return f"please fill the following fields{','.join(missiing_fields)}"
        
        if user:
            
            if cat_id is not None:
                category=category_exists(db_conn,cat_id)

                if category is None:
                    return "Enter a Valid Category Number"
                
                create_note_query(db_conn,user_id,title,content,cat_id)
                return "NOTE CREATED"
            
            create_note_query(db_conn,user_id,title,content,None)
            return "NOTE CREATED"
        else:
            return "USER DOES NOT EXIST"
    else:
        return "Valid json Response required"    
            
            
def update_notes(id):
    if request.cookies.get('user_id') is None:
        return "please login"
    
    if id is None:
        return "Notes ID is required"
    
    if request.is_json:
        
        body=request.get_json()
        title=body.get('Title')
        content=body.get('Content')
        cat_id=body.get('cat_id')
        user_id=request.cookies.get('user_id')
        db_conn=db.mysqlconnection()
        notes=is_notes_exists(db_conn,user_id,id)
        
        if notes:
            update_notes_query(db_conn,user_id,id,title,content,cat_id)
            return "Notes successfully updated","200"
        else:
            return "notes donot exist"
    else:
        return "please return valid json response"
    
def delete_notes(id):
    if request.cookies.get('user_id') is None:
        return "please login"
    
    if id is None:
        return "please enter id"
    
    user_id=request.cookies.get('user_id')
    db_conn=db.mysqlconnection()
    notes=is_notes_exists(db_conn,user_id,id)
    
    if notes:
        delete_notes_query(db_conn,user_id,id)
        return "notes successfully deleted"
    else:
        return "notes not found"
    
def get_all_notes():
    
    if request.cookies.get("user_id") is None:
        return "Please login"
    db_conn=db.mysqlconnection()
    
    user_id=request.cookies.get("user_id")
    result=get_all_notes_query(db_conn,user_id)
    return result
        
    