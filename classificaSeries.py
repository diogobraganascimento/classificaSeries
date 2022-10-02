from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
SECRET_KEY = 'alura'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='root',
        servidor='localhost',
        database='classificaSeries'
    )

db = SQLAlchemy(app)


class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    plataforma = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def index():
    lista = Series.query.order_by(Series.id)
    return render_template('lista.html', titulo='series', series=lista)


app.run(debug=True)
