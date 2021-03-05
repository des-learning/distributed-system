from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)

todos = [{"id": 1, "title": "coba", "finish": False}]

@app.route("/todos", methods=["POST"])
def create():
    body = request.get_json()
    if body is None:
        return jsonify(message="empty request body"), 400
    title = body.get('title', None)
    if title is None or title == '':
        return jsonify(message="missing required parameter title"), 400
    todo_id = len(todos) + 1
    todo = {"id": todo_id, "title": title, "finish": False}
    todos.append(todo)
    return jsonify(id=todo_id), 201

@app.route("/todos", methods=["GET"])
def list_all():
    return jsonify(todos=todos)

@app.route("/todos/<int:todo_id>", methods=["GET"])
def list_one(todo_id):
    if todo_id <= 0 or todo_id > len(todos):
        return jsonify(message=f"todo id {todo_id} not found"), 404
    return jsonify(todo=todos[todo_id-1])
