from flask import Flask
from flask_restful import Api
from app.api.todo import Todo, TodoList
from app.home import home
from app.index import index
from flask import redirect, url_for

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')


@app.route('/')
def page():
    return redirect(url_for('home.index'))

#index page
app.register_blueprint(index, url_prefix='/index')
#home page
app.register_blueprint(home, url_prefix='/home')


#api
api = Api(app)
api.add_resource(TodoList, '/todo/api/v1.0/todos', endpoint = 'todos')
api.add_resource(Todo, '/todos/<todo_id>')
