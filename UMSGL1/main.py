from insert import insert
from update import update
from delete import delete
from read import read

obj = insert()
obj2 = update()
obj3 = delete()
obj4 = read()
print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")

print('------------------------------------------')

print("you can do 4 operations on databse")
print("to inserting data type 'add:'")
print("to updating data type 'update:'")
print("to deleting data type 'delete:'")
print("to raeding data type 'read:'")
opr=input("enter any operation")
if opr=='add':
  print("for inserting the data in department table press-1:")
  print("for inserting the data in course table press-2:")
  print("for inserting the data in faculty table press-3:")
  print("for inserting the data in student table press-4:")

  tab=int(input("please enter the number to insert the data in table:"))
  if tab==1:
     department_id=int(input("please enter the deptid:"))
     department_name=input("please enter the deptname:")
     obj.departmentinsert(department_id,department_name)
  if tab==2:
     course_id=int(input("please enter the courseid:"))
     course_name=input("please enter the coursename:")
     course_fees=int(input("please enter the coursefes:"))
     duration=int(input("please enter the duration:"))
     obj.courseinsert(course_id,course_name,course_fees,duration)
  if tab==3:
     facultyid=int(input("please enter the facultyid:"))
     facultyname=input("please enter the facultyname:")
     salary=int(input("enter the salary:"))
     department_id=int(input("please enter the deptid:"))
     course_id=int(input("please enter the courseid:"))
     obj.faculty1insert(facultyid,facultyname,department_id,salary,course_id)
  if tab==4:
     sid=int(input("please enter the sid:"))
     sname=input("please enter the sname:")
     department_id=int(input("please enter the deptid:"))
     course_id=int(input("please enter the courseid:"))
     obj.studentinsert(sid,sname,department_id,course_id)


     
if opr=='update':
  print("for updating the data in department table press-1:")
  print("for updating the data in course table press-2:")
  print("for updating the data in faculty1 table press-3:")
  print("for updating the data in student table press-4:")

  tab=int(input("please enter the number to update the data in table:"))

  if  tab==1:
      col = input("Please Enter the Colname:")
      old = input("Please enter the olddeptname:")
      new = input("Please Enter the newdeptname:")
      obj2.departmentupdate(colname=col,olddeptname=old,newdeptname=new)
  if tab==2:
     col = input("Please Enter the Colname:")
     old = input("Please enter the oldcoursefees:")
     new = input("Please Enter the newcoursefees:")
     obj2.courseupdate(colname=col,oldcoursefees=old,newcoursefees=new)
  if tab==3:
    col = input("Please Enter the Colid:")
    old = input("Please enter the oldfacid:")
    new = input("Please Enter the newfacid:")
    obj2.faculty1update(colid=col,oldfacid=old,newfacid=new)
  if tab==4:
    col = input("Please Enter the Colid:")
    old = input("Please enter the oldsid:")
    new = input("Please Enter the newsid:")
    obj2.studentupdate(colid=col,oldsid=old,newsid=new)
  

if opr=='delete':
  print("for deleting the data in department table press-1:")
  print("for deleting the data in course table press-2:")
  print("for deleting the data in faculty1 table press-3:")
  print("for deleting the data in student table press-4:")

  tab=int(input("please enter the number to delete the data in table:"))

  if tab==1:
    id = int(input("Please Enter the Department ID to delete data:"))
    obj3.departmentdelete(id)
  if tab==2:
    id = int(input("Please Enter the course id to delete data:"))
    obj3.coursedelete(id)
  if tab==3:
    id = int(input("please Enter the faculty id to delete data:"))
    obj3.faculty1delete(id)
  if tab==4:
    id = int(input("please Enter the student id to delete data:"))
    obj3.studentdelete(id)

  


if opr=='read':
  print("for reading the data in department table press-1:")
  print("for reading the data in course table press-2:")
  print("for reading the data in faculty table press-3:")
  print("for reading the data in student table press-4:")


  tab=int(input("please enter the number to read the data in table:"))

  if tab==1:
    id = int(input("Please Enter the Department ID to read data:"))
    obj4.departmentread(id)
  if tab==2:
    id = int(input("Please Enter the course ID to read data:"))
    obj4.courseread(id)
  if tab==3:
    id = int(input("Please Enter the faculty ID to read data:"))
    obj4.faculty1read(id)
  if tab==4:
    id = int(input("Please Enter the student ID to read data:"))
    obj4.studentread(id)




