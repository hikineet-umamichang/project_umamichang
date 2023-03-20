from flask import Blueprint

main = Blueprint('main', __name__)

# この行の下にビュー関数をインポート
from . import views
