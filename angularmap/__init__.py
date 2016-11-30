from flask import (Flask, render_template)


app = Flask(__name__, static_folder='static')


@app.route('/', methods=["GET"])
def welcomepage():
    """Renders main template named index"""
    return render_template('index.html')

@app.route('/views/main.html', methods=["GET"])
def mainroute():
    """template main render when it is called for"""
    return render_template('main.html')

@app.route('/views/about.html', methods=["GET"])
def aboutroute():
    """ renders the about page """
    return render_template('about.html')
