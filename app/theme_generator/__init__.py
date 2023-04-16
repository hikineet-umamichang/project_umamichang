from flask import Blueprint

theme_generator = Blueprint('theme_generator', __name__)

from . import views
