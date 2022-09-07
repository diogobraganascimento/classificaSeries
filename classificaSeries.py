from flask import Flask, render_template, request


class Serie:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


serie1 = Serie('Luis Miguel', 'BiogrÃ¡fica', 'netflix')
serie2 = Serie('The Witcher', 'Fantasia', 'Netflix')
serie3 = Serie('Hanna', 'aÃ§Ã£o', 'Prime Video')
lista = [serie1, serie2, serie3]


app = Flask(__name__)


@app.route('/inicio')
def index():
    return render_template('lista.html', titulo='series', series=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='nova seria')


@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataaforma']
    serie = Serie(nome, categoria, plataforma)
    lista.append(serie)
    return render_template('lista.html', titulo='Series', series=lista)


app.run()
