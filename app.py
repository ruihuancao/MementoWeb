from flask import Flask
from views.freelancer import freelancer_view
from views.react import react_view
from flask import render_template

app = Flask(__name__)
app.register_blueprint(freelancer_view, url_prefix='/freelancer')
app.register_blueprint(react_view, url_prefix='/react')

@app.route('/')
def hello_world():
    return render_template('index.html')
