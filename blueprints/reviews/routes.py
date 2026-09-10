from flask import Flask, render_template, request, redirect, url_for, session
from blueprints.reviews import reviews_bp

import models

@reviews_bp.route('/review/create', methods=['POST'])
def criar_resenha(livro_id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    if models.buscar_livro(livro_id):
        models.resenhas.append({
            "id": models.proximo_id_resenha,
            "livro_id": livro_id,
            "usuario": session["usuario"],
            "texto": request.form["texto"],
            "nota": int(request.form["nota"]),
        })
        models.proximo_id_resenha += 1
    return redirect(url_for("catalog.ver_livro", livro_id=livro_id))