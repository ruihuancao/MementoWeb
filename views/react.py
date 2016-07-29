__author__ = 'caoruihuan'

from flask import Blueprint
from flask import render_template

react_view = Blueprint('react', __name__)

@react_view.route('/')
def index():
    return render_template('react/index.html')