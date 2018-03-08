from flask import render_template, redirect, url_for, request, g, current_app
from app.main import bp

@bp.route('/test', methods=['GET'])
def test():
    return 'HelloWorld!'

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')
