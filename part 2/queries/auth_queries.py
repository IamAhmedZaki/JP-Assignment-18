import bcrypt



def registration_checking(db_conn,username,email):
    query="SELECT * from users WHERE username=%s or email=%s"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(username,email))
    result=mycursor.fetchall()
    return result

def create_user(db_conn,username,email,hash):
    query="INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(username,email,hash))
    db_conn.commit()
    return "user created successfully"

def check_user(db_conn, username, password):
    query="SELECT password,id from users WHERE username=%s"
    mycursor=db_conn.cursor()
    mycursor.execute(query,(username,))
    result=mycursor.fetchone()
    if result:
        hashed_password=result['password']
        if bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8')):
            return result['id']
        else:
            return False
    else:
        return None
    #query = 'SELECT password,id FROM users WHERE username=%s'
    
    # try:
    #     with db_conn.cursor() as cur:
    #         cur.execute(query, (username,))
    #         result = cur.fetchone()
    #         # print('result user',result['password'])
    #         if result:
    #             stored_password_hash = result['password']
    #             if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
    #                 return result['id'] 
    #             else:
    #                 return False 
    #         else:
    #             return None 
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     return None