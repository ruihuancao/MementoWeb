__author__ = 'caoruihuan'

from flask import render_template
from . import index

@index.route('/')
def index(name=None):
    item = {'url':'http://placehold.it/400x300', 'alt':'test'}
    data = [item for i in range(100)]
    title = 'test'
    return render_template('index.html', name=name, data = data, title=title)

