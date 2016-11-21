from flask import Blueprint

react = Blueprint(
    'react',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views