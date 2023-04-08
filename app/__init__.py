import os
import logging
from flask import Flask, Blueprint, send_from_directory
from .main import main as main_blueprint
from .weather import weather as weather_blueprint
from .wordwolf import wordwolf as wordwolf_blueprint
from app.blog import blog as blog_blueprint
from .mail import mail as mail_blueprint


def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get("SECRET_KEY")


    app.config['LOG_LEVEL'] = logging.DEBUG
    file_handler = logging.FileHandler('flask_app.log')
    file_handler.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(file_handler)


    app.register_blueprint(main_blueprint)
    app.register_blueprint(weather_blueprint)
    app.register_blueprint(wordwolf_blueprint, url_prefix="/wordwolf")
    app.register_blueprint(blog_blueprint, url_prefix="/blog")
    app.register_blueprint(mail_blueprint, url_prefix="/mail")



    # blog_posts/images用のBlueprintを作成
    blog_images_bp = Blueprint("blog_images", __name__, url_prefix="/images")

    @blog_images_bp.route("/<path:filename>")
    def blog_images(filename):
        return send_from_directory("../blog_posts/images", filename)

    app.register_blueprint(blog_images_bp)



    return app
