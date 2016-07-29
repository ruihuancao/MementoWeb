from flask import Flask
from flask import render_template

from views.freelancer import index_view

app = Flask(__name__)


app = Flask(__name__)

app.register_blueprint(index_view, url_prefix='/freelancer')

@app.route('/')
def hello_world():
    return 'Hello World!'
