from flask import Flask
from .main import main as main_blueprint
from .weather import weather as weather_blueprint
from .wordwolf import wordwolf as wordwolf_blueprint
from app.blog import blog as blog_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(weather_blueprint)
    app.register_blueprint(wordwolf_blueprint, url_prefix="/wordwolf")
    app.register_blueprint(blog_blueprint, url_prefix="/blog")

    return app
