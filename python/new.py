
import pymysql as sql

def db_connect():
    conn=sql.connect(host='localhost',port=3306,user='root',password='',database='Event')
    cur=conn.cursor()
    return conn,cur

def signup():
    cmd=f"insert into user values ('renu', 'pareta', '3784')"
    conn,cur=db_connect()
    cur.execute(cmd)
    conn.commit()
    
    
signup()   


