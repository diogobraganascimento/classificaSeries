from flask import Flask, render_template, request, redirect, session, flash


class Serie:
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


serie1 = Serie('Luis Miguel', 'biografia', 'netflix')
serie2 = Serie('The Witcher', 'Fantasia', 'Netflix')
serie3 = Serie('Hanna', 'acao', 'Prime Video')
lista = [serie1, serie2, serie3]

app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    return render_template('lista.html', titulo='series', series=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='nova serie')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    serie = Serie(nome, categoria, plataforma)
    lista.append(serie)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123456' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuário logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado!')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


app.run(debug=True)
