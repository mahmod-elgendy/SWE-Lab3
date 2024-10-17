from flask import Blueprint, request, jsonify
from middleware.auth import authenticationToken


todos = []
todos_bp = Blueprint ("todos", __name__)

students = {"id": 202201483, 
            "name": "Mahmoud Elgendy"}


todo = students

@todos_bp.before_request
def before_request():
    authenticationToken()


@todos_bp.route("/", methods=["GET"]) 
def get_todos():
    return jsonify(todo)


@todos_bp.route("/", methods=["POST"]) 
def create_todo():
    todo = {
    "id": len(todos) + 1,
    "title": request.json.get("title"),
    "completed": request.json.get("completed", False),
    }
    todos.append(todo)
    return jsonify (todo), 201



@todos_bp.route("/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 484 
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"]) 
    return jsonify (todo)


@todos_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t["id"] != id]
    return '', 204