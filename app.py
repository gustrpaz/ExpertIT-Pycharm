from flask import Flask, render_template, request, redirect
from lista import candidatos
from usuario import Usuario,usuarios

app = Flask(__name__)


@app.route('/')
def landingpage(): 
    return render_template("landingpage.html")

@app.route('/cursos')
def cursos(): 
    return render_template("cursos.html")

@app.route('/formulario')
def formulario():  
    return render_template("formulario.html", usuarios=usuarios)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome, email, senha)
    usuarios.append(usuario)
    return redirect('/formulario')

@app.route('/professores')
def professores():  
    return render_template("professores.html", lista=candidatos)

if __name__ == '__main__':
    app.run(debug=True)
