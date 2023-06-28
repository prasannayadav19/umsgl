import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums1',
    user='root',
    password='prasanna@0919'
)

cur  = conn.cursor()

class insert:
    def departmentinsert(x,department_id,department_name):
        cur.execute(f"insert into department values({department_id},'{department_name}')")
        conn.commit()
        print("data has been inserted successfully")

    def courseinsert(x,course_id,course_name,course_fees,duration):
        cur.execute(f"insert into course values({course_id},'{course_name}',{course_fees},{duration})")
        conn.commit()
    
    def faculty1insert(x,facultyid,facultyname,departmentid,salary,courseid):
        cur.execute(f"insert into faculty1 values({facultyid},'{facultyname}',{departmentid},{salary},{courseid})")
        conn.commit()

    def studentinsert(x,sid,sname,departmentid,courseid):
        cur.execute(f"insert into student values({sid},'{sname}',{departmentid},{courseid})")
        conn.commit()







