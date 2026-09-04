from flask import Flask, render_template, request, session, redirect, url_for, flash

import models as models


app = Flask(__name__)
app.secret_key = "chave-secreta"

def verifyLogin():
    if not "usuario" in session:
        return redirect(url_for('login'))

@app.route('/', methods=['GET'])
def index():
    livros = models.buscar_livros()
    if not "usuario" in session:
        nome_usuario = None
    else: 
        nome_usuario = session["usuario"]
    return render_template('index.html', livros=livros,  nome_usuario=nome_usuario)

@app.route('/livro-detalhe/<int:livro_id>', methods=['GET'])
def livro_detalhe(livro_id):
    if not livro_id:
        return ('Livro não encontrado', 404)
    
    livro = models.buscar_livro(livro_id)

    if not livro:
        return ('Livro não encontrado', 404)
    
    resenhas = models.resenhas_do_livro(livro_id)

    return render_template('livro-detalhe.html', livro=livro, resenhas=resenhas)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if "usuario" in session:
            return redirect(url_for('index'))
        return render_template('login.html')
    
    
    
    nome = request.form.get('nome')
    senha =  request.form.get('senha')

    if (models.loginIsTrue(nome, senha)):
        session["usuario"] = nome
        return redirect(url_for('index'))
    
    flash('nome ou senhas inválidos', 'erro')
    return render_template('login.html'), 401

@app.route('/logout', methods=['GET'])
def logout():

    session.pop("usuario", None)
    return redirect(url_for('index'))

# @app.route('/')

    
    

