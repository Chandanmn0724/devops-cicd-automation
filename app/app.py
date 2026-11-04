from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn DevOps", "status": "In Progress"},
    {"id": 2, "title": "Build CI/CD Pipeline", "status": "Pending"},
    {"id": 3, "title": "Deploy using Docker", "status": "Pending"}
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Task Manager",
        "status": "Application is running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

