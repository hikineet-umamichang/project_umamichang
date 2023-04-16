from flask import render_template
from . import theme_generator

@theme_generator.route('/theme_generator')
def index():
    return render_template('theme_generator/index.html')
