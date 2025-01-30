from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todo = []

@app.route("/")
def index():
    return render_template("home.html", todo=todo)

@app.route("/add", methods=["POST"])
def add():
    todo_name = request.form.get('todo')
    if todo_name:
        todo.append({"id": len(todo), "name": todo_name, "completed": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id):
    edited_name = request.form.get('edit')
    for todos in todo:
        if todos['id'] == todo_id and edited_name:
            todos['name'] = edited_name
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    global todo
    todo = [todos for todos in todo if todos['id'] != todo_id]
    return redirect(url_for("index"))

@app.route("/toggle/<int:todo_id>")
def toggle_todo(todo_id):
    for todos in todo:
        if todos['id'] == todo_id:
            todos["completed"] = not todos["completed"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
