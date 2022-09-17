from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Serie, Usuario
from dao import SerieDao, UsuarioDao
import os
import time
from helpers import deleta_arquivo, recupera_imagem
from classificaSeries import db, app


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
    serie = serie_dao.salvar(serie)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{serie.id}-{timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    serie = serie_dao.busca_por_id(id)
    print(serie)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Serie', serie=serie, capa_serie=nome_imagem or 'capa_padrao.jpg')



@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    serie = Serie(nome, categoria, plataforma, id=request.form['id'])

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(serie.id)
    arquivo.save(f'{upload_path}/capa{serie.id}-{timestamp}.jpg')
    serie_dao.salvar(serie)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    serie_dao.deletar(id)
    flash('A serie foi removida com sucesso!')
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


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)