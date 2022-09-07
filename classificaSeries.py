from flask import Flask, render_template


class Serie:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


app = Flask(__name__)


@app.route('/inicio')
def index():
    serie1 = Serie('Luis Miguel', 'BiogrÃ¡fica', 'netflix')
    serie2 = Serie('The Witcher', 'Fantasia', 'Netflix')
    serie3 = Serie('Hanna', 'aÃ§Ã£o', 'Prime Video')
    lista = [serie1, serie2, serie3]
    return render_template('lista.html', titulo='series', series=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='nova seria')


app.run()
