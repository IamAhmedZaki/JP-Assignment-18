import db
from flask import request, jsonify

def checkuser_exists(db_conn,user_id):
    query="SELECT id, username, email from users WHERE id=%s"
    
    mycursor=db_conn.cursor()
    mycursor.execute(query,(user_id))
    result=mycursor.fetchall()
    return result if result else None


def category_exists(db_conn, cat_id):
    query="SELECT * from category WHERE id=%s"
    
    mycursor=db_conn.cursor()
    mycursor.execute(query,(cat_id))
    result=mycursor.fetchall()
    return result if result else None


def create_note_query(db_conn,user_id,title,content,cat_id):
    query="INSERT INTO notes (user_id,title,content,cat_id) VALUES (%s,%s,%s,%s)"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(user_id,title,content,cat_id))
    db_conn.commit()
    result=mycursor.fetchall()
    
    return result if result else None

def is_notes_exists(db_conn,user_id,id):
    query="SELECT * FROM notes where id=%s and user_id=%s"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(id,user_id))
    result=mycursor.fetchall()
    return result if result else None

def update_notes_query(db_conn,user_id,id,title=None,content=None,cat_id=None):
    query="UPDATE notes Set"
    fields=[]
    if title is not None:
        query+=" title=%s "
        fields.append(title)
    
    if content is not None:
        query+=" ,content=%s "
        fields.append(content)
        
    if cat_id is not None:
        query+=" ,cat_id=%s "
        fields.append(cat_id)
    
    if title is None and content is None and cat_id is None:
        return " no changes were made"
    
    if user_id and id:
        query+="  WHERE id=%s and user_id=%s"
        fields.append(id)
        fields.append(user_id)
        
    mycursor=db_conn.cursor()
    mycursor.execute(query,(fields))
    db_conn.commit()
    result=mycursor.fetchall()
    return result if result else None


def delete_notes_query(db_conn,user_id,id):
    query="Delete from notes WHERE user_id=%s and id=%s"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(user_id,id))
    db_conn.commit()
    print("notes deleted query activated")
    
def get_all_notes_query(db_conn,user_id):
    query="SELECT * FROM notes "
    title=request.args.get('title')
    
    if title:
        query+=" WHERE user_id=%s AND title=%s"
        mycursor=db_conn.cursor()
        mycursor.execute(query,(user_id,title))
        result=mycursor.fetchall()
        return result if result else None
    
    query+=" WHERE user_id=%s"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(user_id))
    result=mycursor.fetchall()
    return result if result else None