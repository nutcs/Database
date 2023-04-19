import sqlite3

conn = sqlite3.connect('hw13_1650704388.db')
cursor = conn.cursor()

#ดูข้อมูล
def listenDB():
    sql = 'select * from students'
    cursor.execute(sql)
    showDb = cursor.fetchall()
    print(showDb,'\n')

#เพิ่มข้อมูล
def addData_DB():
    sql = "insert into students values(?,?,?,?,?,?,?)"
    cursor.execute(sql,[1650700003, 'Nutthapon2', 'Salangsing3', 'male', 19, 'nut3', 'n3'])
    conn.commit()

#อัปเดตข้อมูล
def updateDB():
    # std_id  /  first_name  /  lastname  /  gender  /  year  /  username  / password
    #update students set password=? username=? where std_id=?;
    sql = """
    update students set password=? where std_id=?;
    """
    cursor.execute(sql,['ng',1])
    conn.commit()

#ลบข้อมูล
def deleteDB():
    sql = "delete from students where std_id=?;"
    cursor.execute(sql,[1])
    conn.commit()


#listenDB()
#updateDB()
#deleteDB()
#addData_DB()
listenDB()
conn.close()