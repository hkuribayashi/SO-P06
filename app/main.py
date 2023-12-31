from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'minhasenha'
app.config['MYSQL_DB'] = 'meubanco'
 
mysql = MySQL(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO dados VALUES(NULL,%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Feito!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
