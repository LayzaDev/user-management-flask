from flask import Flask, render_template, request, redirect, url_for
from operations import create, read, update, delete 
from db_connection import initialize_db

app = Flask(__name__)

initialize_db()

@app.route('/')
def index():
    users = read()
    return render_template('/index.html', users=users)

@app.route('/create', methods=(['GET', 'POST']))
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        profession = request.form['profession']
        phone = request.form['phone']
        create(name, int(age), profession, phone)
        return redirect(url_for('/index'))
    return render_template('/create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    users = read()
    user = next((user for user in users if user[0] == id), None)
    if user is None:
        return "Usuário não encontrado.", 404
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        profession = request.form['profession']
        phone = request.form['phone']
        update(id, name, int(age), profession, phone)
        return redirect(url_for('/index'))
    return render_template('/update.html', user=user)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
    delete(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)