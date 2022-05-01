from flask import Blueprint, render_template

bp = Blueprint("operations", __name__)

@bp.route("/")
def home():
    return render_template("operations/home.html")
