from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"tasks": "samples", "done": False}]


def count_completed_tasks():
    return sum(1 for todo in todos if todo['done'])


def count_total_tasks():
    return len(todos)


# Custom Jinja2 filter for enumerate-like functionality
def jinja2_enumerate(iterable, start=0):
    return zip(range(start, start + len(iterable)), iterable)


# Adding the custom filter to the Jinja2 environment
app.jinja_env.filters['enumerate'] = jinja2_enumerate


@app.route('/')
def index():
    completed = count_completed_tasks()
    total = count_total_tasks()
    return render_template('index.html', todos=todos, completed=completed, total=total)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'tasks': todo, 'done': False})
    return redirect(url_for("index"))


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['tasks'] = request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route('/check/<int:index>', methods=['POST', 'PATCH'])
def check(index):
    if request.method == 'POST' or request.form.get('_method') == 'PATCH':
        todos[index]['done'] = not todos[index]['done']
        return redirect(url_for("index"))


@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
