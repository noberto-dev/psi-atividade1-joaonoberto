from flask import Flask, render_template, request, redirect, url_for, session, abort
from blueprints.errors import errors_bp
import models


@errors_bp.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

