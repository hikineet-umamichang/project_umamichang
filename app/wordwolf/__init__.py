from flask import Blueprint

wordwolf = Blueprint('wordwolf', __name__, template_folder='templates/wordwolf')

from . import views
