from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

todos = ["Buy groceries", "Read a book","learn python"]

@app.route('/')
def index():
    return redirect(url_for('todo'))    

@app.route('/todos', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        new_todo = request.form.get('todo')
        if new_todo:
            todos.append(new_todo)
        return redirect(url_for('todo')) # redirect to the same page to prevent the Post/Redirect/Get (PRG) pattern
    elif request.method == 'GET':
        return render_template('todos.html', todos=todos)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if id < len(todos):
        todos.pop(id)
    return redirect(url_for('todo'))
if __name__ == '__main__':
    app.run(debug=True)
