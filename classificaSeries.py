from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import Serie, Usuario
from dao import SerieDao, UsuarioDao
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'alura'

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "classificaSeries"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

serie_dao = SerieDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = serie_dao.listar()
    return render_template('lista.html', titulo='series', series=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='nova serie')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    serie = Serie(nome, categoria, plataforma)
    serie_dao.salvar(serie)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.nome
            flash(usuario.nome + 'Usuário logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado!') 
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)
