from flask import Flask,render_template, request

from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskdb'
mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']

        cur=mysql.connection.cursor()

        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return 'record insert successfully'
    return render_template('index.html')

@app.route('/users')
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('user.html', users=users)


if __name__ == '__main__':
    app.run()