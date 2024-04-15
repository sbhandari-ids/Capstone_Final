from flask import Blueprint

admin = Blueprint('admin', __name__ , template_folder='admin_templates', static_folder='static')

from app.blueprints.admin import routes

from . import forms
