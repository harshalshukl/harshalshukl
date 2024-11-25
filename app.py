import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database (can be replaced with a proper database)
tasks = []

# Get GEN_API from environment variables
GEN_API = os.getenv("GEN_API", "123456789")

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, gen_api=GEN_API)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
