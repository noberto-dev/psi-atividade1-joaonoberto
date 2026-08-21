from flask import Flask, render_template, request, session, redirect, url_for

import models as models


app = Flask(__name__)
app.secret_key = "chave-secreta"


@app.route('/', methods=['GET'])
def index():
    livros = models.buscar_livros()

    return render_template('index.html', livros=livros)

@app.route('/livro-detalhe/<int:livro_id>', methods=['GET'])
def livro_detalhe(livro_id):
    livro = models.buscar_livro(livro_id)

    if not livro:
        return ('Página não encontrada', 404)
    
    resenhas = models.resenhas_do_livro(livro_id)

    return render_template('livro-detalhe.html', livro=livro, resenhas=resenhas)

@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    nome = request.form.get('nome')
    senha =  request.form.get('senha')

    if (models.loginIsTrue(nome, senha)):
        session['usuario'] = nome
        return redirect(url_for('index'))
    

