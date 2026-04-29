import uuid
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = {}


def validate_task_input(data, require_title=True):
    errors = []
    if require_title and not data.get("title"):
        errors.append("title is required")
    if "priority" in data and data["priority"] not in ("low", "medium", "high"):
        errors.append("priority must be one of: low, medium, high")
    if "status" in data and data["status"] not in ("todo", "in_progress", "done"):
        errors.append("status must be one of: todo, in_progress, done")
    return errors


# BUG 1: route should be /tasks
@app.route("/task", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    errors = validate_task_input(data)
    if errors:
        return jsonify({"error": "; ".join(errors)}), 400
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"],
        "priority": data.get("priority", "medium"),
        "status": data.get("status", "todo"),
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    tasks[task_id] = task
    # BUG 2: should return 201
    return jsonify(task), 200


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json(silent=True) or {}
    for field in ("title", "priority", "status"):
        if field in data:
            # BUG 3: should update task[field]
            pass
    return jsonify(task), 200


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    del tasks[task_id]
    # BUG 4: should return 204 with empty body
    return jsonify({"deleted": True}), 200


# BUG 5: missing runnable entry point with app.run
