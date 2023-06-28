import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums1',
    user='root',
    password='prasanna@0919'
)

cur  = conn.cursor()

class read:
    def departmentread(x,id):
      cur.execute(f"select * from department where department_id={id}")
      print(cur.fetchall())
    
    def courseread(x,id):
       cur.execute(f"select * from course where course_id={id}")
       print(cur.fetchall())
    
    def faculty1read(x,id):
       cur.execute(f"select * from faculty1 where facultyid={id}")
       print(cur.fetchall())
    
    def studentread(x,id):
       cur.execute(f"select * from student where sid={id}")
       print(cur.fetchall())
       