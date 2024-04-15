from flask import Blueprint

main = Blueprint('main', __name__ , template_folder='main_templates', static_folder='static')

from . import routes 