from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Learn CI/CD"}
]


@app.route("/")
def home():
    return "Welcome to TaskPilot API!"


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"]
    }

    tasks.append(new_task)

    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)