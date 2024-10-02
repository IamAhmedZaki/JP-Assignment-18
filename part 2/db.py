import pymysql

def mysqlconnection():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password="ahmedzaki", # empty password
        db='notes',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print("db connected")
    return conn
    

def diconnect(conn):
  conn.close()

if __name__ == "__main__":
    mysqlconnection()