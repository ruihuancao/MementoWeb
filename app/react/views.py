__author__ = 'caoruihuan'

from flask import render_template
from . import react

@react.route('/')
def index():
    return render_template('react/index.html')