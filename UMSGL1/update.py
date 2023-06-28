import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums1',
    user='root',
    password='prasanna@0919'
)

cur  = conn.cursor()

class update:
    def departmentupdate(x,colname,newdeptname,olddeptname):
        cur.execute(f"update department set {colname}='{newdeptname}' where {colname}='{olddeptname}'")
        conn.commit()
      #obj = update()
          #obj.departmentupdate('department_name','goa','D1')
   
    def courseupdate(x,colname,newcoursefees,oldcoursefees):
        cur.execute(f"update course set {colname}='{newcoursefees}' where {colname}='{oldcoursefees}'")
        conn.commit()


    def faculty1update(x,colid,newfacid,oldfacid):
        cur.execute(f"update faculty1 set {colid}={newfacid} where {colid}={oldfacid}")
        conn.commit()

    def studentupdate(x,colid,newsid,oldsid):
        cur.execute(f"update student set {colid}={newsid} where {colid}={oldsid}")
        conn.commit()



    