from flask import Flask
from flask_restful import Api
from views.freelancer import freelancer_view
from views.react import react_view
from flask import render_template

from api.todo import Todo, TodoList


app = Flask(__name__)
api = Api(app)

app.register_blueprint(freelancer_view, url_prefix='/freelancer')
app.register_blueprint(react_view, url_prefix='/react')

# api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint = 'tasks')
api.add_resource(TodoList, '/todo/api/v1.0/todos', endpoint = 'todos')
api.add_resource(Todo, '/todos/<todo_id>')


@app.route('/')
def hello_world():
    return render_template('index.html')

