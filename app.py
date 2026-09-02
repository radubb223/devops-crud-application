from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'flash message'
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud_flask_app'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close
    return render_template('app.html', students=data)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        pincode = request.form['pincode']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO students (name, email, phone, address, city, pincode) VALUES (%s, %s, %s, %s, %s, %s)',
                    (name, email, phone, address, city, pincode))
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        pincode = request.form['pincode']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE students
            SET name=%s,
                email=%s,
                phone=%s,
                address=%s,
                city=%s,
                pincode=%s
            WHERE id=%s
        """, (name, email, phone, address, city, pincode, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods=['POST', 'GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id={0}".format(id_data))
    mysql.connection.commit()
    return redirect(url_for('index'))

def init_db():
    with app.app_context():
        cur = mysql.connection.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(20),
                address VARCHAR(255),
                city VARCHAR(100),
                pincode VARCHAR(20)
            )
        """)

        mysql.connection.commit()
        cur.close()

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=5000)
