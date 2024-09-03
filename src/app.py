from flask import Flask, render_template, request ,redirect,url_for, session
from config import *
from registro import registroInventario
#import bcrypt

con_bd =conexionbd()
app=Flask(__name__) 

"""
#
app.secret_key = "mysecret"

#
@app.route('/')
def home():
    if 'nombre' in session:
        return f'Bienvenido, {session["nombre"]} <a href="/logout">Cerrar sesión</a>'
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        personas =con_bd['personas']
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        user = personas.find_one({'nombre': nombre})
        if user and bcrypt.checkpw(contrasena.encode('utf-8'), user['contrasena']):
            session['nombre'] = nombre
            return redirect('/')
        else:
            return 'Credenciales inválidas. <a href="/login">Intentar de nuevo</a>'
    else:
        return render_template('login.html')

@app.route('/mostrar', methods=['GET', 'POST'])
def guardar_producto():
    if request.method == 'POST':
        personas =con_bd['personas']
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
        personas.insert_one({'nombre': nombre, 'contrasena': hashed_password})
        return redirect('/login')
    else:
        return render_template('mostrar.html')


@app.route('/logout')
def logout():
    session.pop('nombre', None)
    return redirect('/')

"""

@app.route('/') 
def index():  
    coleccionPersonas =con_bd['personas']
    PersonasRegistradas = coleccionPersonas.find()
    return render_template('index.html', datos = PersonasRegistradas)


@app.route('/guardar_producto',methods=['POST']) 
def agregarPersona():
    personas =con_bd['personas']

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    contrasena = request.form['contrasena']

    if id and nombre and apellido and correo and contrasena: 
        persona1 = registroInventario( nombre,apellido,correo,contrasena)
        personas.insert_one(persona1.formato_doc())
        return redirect(url_for('index'))
    else:
        return render_template('login')
 
"""  
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        personas =con_bd['personas']
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        user = personas.find_one({'nombre': nombre})
        if user and bcrypt.checkpw(contrasena.encode('utf-8'), user['contrasena']):
            session['nombre'] = nombre
            return redirect('/')
        else:
            return 'Credenciales inválidas. <a href="/login">Intentar de nuevo</a>'
    else:
        return render_template('login.html')    
    



@app.route('/eliminar_persona/<string:nombre_persona>') 
def eliminar (nombre_persona):
    personas =con_bd['personas'] 
    personas.delete_one({'nombre': nombre_persona})
    return redirect(url_for('index'))

@app.route('/editar_persona/<string:nombre_persona>' ,methods=['POST'] ) 
def editar (nombre_persona):
    personas =con_bd['personas'] 

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    
    if nombre and apellido and correo and contrasena:
        personas.update_one({'nombre':nombre_persona},{'$set':{'nombre':nombre, 'apellido':apellido, 'correo': correo, 'contrasena': contrasena}})
    else :
        return "Error "
            
    return redirect(url_for('mostrar'))
"""

@app.route('/login') 
def login():
    return render_template('login.html')

@app.route('/mostrar', methods=['GET']) 
def mostrar ():
    return render_template('mostrar.html')

@app.route('/modulos', methods=['GET']) 
def modulos ():
    return render_template('modulos.html')

@app.route('/guardar_producto', methods=['GET']) 
def guardar_producto ():
    return render_template('index.html') 

@app.route('/perfil', methods=['GET']) 
def perfil ():
    return render_template('perfil.html') 

@app.route('/datos', methods=['GET']) 
def datos ():
    return render_template('datos.html') 

    
if __name__=='__main__':
    app.run(debug=True, port=5000)

