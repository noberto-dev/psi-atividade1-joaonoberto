from flask import Flask, render_template, request, redirect, url_for, session
from blueprints.catalog import catalog_bp
import models

@catalog_bp.route("/")
def index():
    q = request.args.get("q", "")
    return render_template("index.html", livros=models.buscar_livros(q), q=q)

@catalog_bp.route("/livro/<int:livro_id>")
def ver_livro(livro_id):
    livro = models.buscar_livro(livro_id)
    if livro is None:
        return "Livro não encontrado", 404
    return render_template("livro-detalhe.html", livro=livro,
        resenhas=models.resenhas_do_livro(livro_id))

