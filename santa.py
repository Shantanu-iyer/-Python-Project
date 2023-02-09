from flask import Flask, render_template,request
from flask_mysqldb import MySQL
s=Flask(__name__)
mysql=MySQL(s)
s.config['MYSQL_HOST'] = 'localhost'
s.config['MYSQL_USER'] = 'root'
s.config['MYSQL_PASSWORD'] = ''
s.config['MYSQL_DB'] = 'python_project'
@s.route('/')
def first():
    return render_template('intro.html')

@s.route('/s')
def second():
    return render_template("fpage.html")

@s.route('/t',methods=['GET', 'POST']) 
def third():
    if request.method=='POST':
        name=request.form.get('username',"")
        email_id=request.form.get('emailid',"")
        print(name)
        print(email_id)
        cursor = mysql.connection.cursor()
        cursor.execute(" INSERT INTO userdetail VALUES(%s,%s)",(name,email_id))
        mysql.connection.commit()
        cursor.close()

    return render_template("spage.html")

if __name__=="__main__":
    s.run(debug=True)