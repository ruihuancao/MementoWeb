from flask import Flask
from flask_restful import Api
from flask import render_template
from api.todo import Todo, TodoList

from .home import home
from .react import react


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
#app.config.from_envvar('APP_CONFIG_FILE')


@app.route('/')
@app.route('/<name>')
def index(name=None):
    item = {'url':'http://placehold.it/400x300', 'alt':'test'}
    data = [item for i in range(100)]
    title = 'test'
    return render_template('index.html', name=name, data = data, title=title)


app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(react, url_prefix='/react')

api = Api(app)
api.add_resource(TodoList, '/todo/api/v1.0/todos', endpoint = 'todos')
api.add_resource(Todo, '/todos/<todo_id>')
