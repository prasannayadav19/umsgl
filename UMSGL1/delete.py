import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums1',
    user='root',
    password='prasanna@0919'
)

cur  = conn.cursor()

class delete:
    def departmentdelete(x,id):
      cur.execute(f"delete from department where department_id={id}")
      conn.commit()
    #obj = delete()
 #obj.departmentdelete(2)
    def coursedelete(x,id):
       cur.execute(f"delete from course where course_id={id}")
       conn.commit()

    def faculty1delete(x,id):
       cur.execute(f"delete from faculty1 where facultyid={id}")
       conn.commit()

    def studentdelete(x,id):
       cur.execute(f"delete from student where sid={id}")
       conn.commit()
       
      