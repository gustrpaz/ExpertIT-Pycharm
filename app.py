from flask import Flask, render_template
from lista import candidatos

app = Flask(__name__)


@app.route('/')
def landingpage():  # put application's code here
    return render_template("landingpage.html")

@app.route('/cursos')
def cursos():  # put application's code here
    return render_template("cursos.html")

@app.route('/formulario')
def formulario():  # put application's code here
    return render_template("formulario.html")

@app.route('/teste')
def teste():  # put application's code here
    lista = ['Rodrigo',
             'Gustavo', 'Enzo', 'Guilherme']
    #return render_template("teste.html", jogos="Jogos", game=game)
    return render_template("teste.html", lista=candidatos)

if __name__ == '__main__':
    app.run(debug=True)
