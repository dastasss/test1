from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'fichamedica'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    
    return render_template('index.html')

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        rut = request.form['rut']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        email = request.form['email']
        fecha = request.form['fecha'] 
        ecivil = request.form['ecivil']
        comentarios = request.form['comentarios']      
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pacientes  (nombre, apellido, rut, telefono, direccion, ciudad, email, fecha, ecivil,comentarios) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nombre, apellido,rut, telefono,direccion,ciudad,email,fecha,ecivil,comentarios))
        mysql.connection.commit()
        flash('Paciente agregado')
        return redirect(url_for('Index'))













# levantar app en puerto 3000 con debug en true para plaicar cambios en vivo
if __name__ == "__main__":
    app.run(port=3000, debug=True)