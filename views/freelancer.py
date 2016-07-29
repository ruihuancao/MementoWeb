__author__ = 'caoruihuan'

from flask import Blueprint
from flask import render_template

freelancer_view = Blueprint('freelancer', __name__)

@freelancer_view.route('/')
def index():
    return render_template('freelancer/index.html')

