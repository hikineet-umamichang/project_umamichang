from flask import Flask
from .config import Config
from .main import main as main_blueprint
from .weather import weather as weather_blueprint
from .wordwolf import wordwolf as wordwolf_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(weather_blueprint)
    app.register_blueprint(wordwolf_blueprint, url_prefix='/wordwolf')

    return app
