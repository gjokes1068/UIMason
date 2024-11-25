from flask import Blueprint
from flask import render_template

main_bp = Blueprint('main', __name__)

@main_bp.get('/')
def canvas():
    return render_template('canvas.html')
