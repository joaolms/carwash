from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/login')
def login():
    return 'página de login'


@app.route('/agendamentos')
def agendamentos_lista():
    return 'lista de agendamentos'


@app.route('/agendamentos/novo')
def agendamento_cadastro():
    return 'cadastro agendamento'


@app.route('/clientes')
def clientes_lista():
    return 'lista clientes'


@app.route('/clientes/novo')
def clientes_cadastro():
    return 'cadastro clientes'


@app.route('/veiculos')
def veiculos_lista():
    return 'lista de veículos'


@app.route('/veiculos/novo')
def veiculos_cadastro():
    return 'cadastro de veículos'


@app.route('/servicos')
def servicos_lista():
    return 'lita de serviços'


@app.route('/servicos/novo')
def servicos_cadastro():
    return 'cadastro de serviços'


if __name__ == "__main__":
    app.run(debug=True)
