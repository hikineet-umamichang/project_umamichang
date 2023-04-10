from flask import render_template, request
from . import test

@test.route('/test')
def test_page():
    return render_template('test/test.html')
