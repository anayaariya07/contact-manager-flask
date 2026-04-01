from flask import Flask, render_template, request, redirect
from dbhelper import DBHelper

app = Flask(__name__)
db = DBHelper()

# HOME - show all contacts
@app.route('/')
def index():
    users = db.fetch_all()
    return render_template('index.html', users=users)

# ADD USER
@app.route('/add', methods=['POST'])
def add_user():
    userid = request.form.get('userid')
    name = request.form.get('username')
    phone = request.form.get('phone')

    db.insert_user(userid, name, phone)
    return redirect('/')

# DELETE USER
@app.route('/delete/<int:id>')
def delete_user(id):
    db.delete_user(id)
    return redirect('/')

# UPDATE USER
@app.route('/update', methods=['POST'])
def update_user():
    userid = request.form.get('userid')
    name = request.form.get('username')
    phone = request.form.get('phone')

    db.update_user(userid, name, phone)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)