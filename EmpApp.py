from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *



app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'department'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('attendance.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')


@app.route("/addAttend", methods=['POST'])
def AddAttend():
    attendance_ID = request.form['attendance_ID']
    emp_ID = request.form['emp_ID']
    attendance_date = request.form['attendance_date']
    attendance_status = request.form['attendance_status']
    
    

    insert_sql = "INSERT INTO attendance VALUES (%s, %s, %s, %s)"
    cursor = db_conn.cursor()


    try:

        cursor.execute(insert_sql, (attendance_ID, emp_id, attendance_date, attendance_status))
        db_conn.commit()
        
    finally:
        cursor.close()

    print("all modification done...")
    return render_template('attendance.html')
    
 
   
  
@app.route("/fetchdata", methods=['POST'])
def fetchdata():
   
    select_employee_query = "SELECT * FROM attendance"
    cursor = db_conn.cursor():
    
    cursor.execute(select_employee_query)
    db_conn.commit():
    result = cursor.fetchall()
    for row in result:
        print(row)
    return render_template('GetEmpOutput.html', attendance_ID=attendance_ID, emp_id=emp_id, attendance_date=attendance_date, attendance_status=attendance_status)

@app.route("/showData", methods=['POST'])
def showData():

    attendance_ID = request.form['attendance_ID']
    select_employee_query = "SELECT * FROM attendance WHERE attendance_ID=%s"
    cursor = db_conn.cursor():
    
    cursor.execute(select_employee_query,(attendance_ID))
    db_conn.commit():
    
    for i in cursor:
       attendance_ID = i[0]
       emp_id = i[1]
       attendance_date = i[2]
       attendance_status = i[3]
       
    cursor.close()   
    return render_template('GetEmpOutput.html', attendance_ID=attendance_ID, emp_id=emp_id, attendance_date=attendance_date, attendance_status=attendance_status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

