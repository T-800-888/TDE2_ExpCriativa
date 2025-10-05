from flask import Blueprint, request, render_template, redirect
from flask_login import UserMixin, login_user, logout_user, login_required

class User(UserMixin):
    def __init__(self, id):
        self.id = id
    @staticmethod
    def get(user_id):
        if user_id in users:
            return User(user_id)
        return None

login = Blueprint("login", __name__ , template_folder="templates")

users = {
    'user1': '1234',
    'user2': '1234'
}

@login.route('/home')
@login_required
def home():
    return render_template("home.html")

@login.route('/login', methods=['GET', 'POST'])
def validated_user():
    if request.method == 'POST':
        user_id = request.form['user']
        password = request.form['password']

        if user_id in users and users[user_id] == password:
            user = User.get(user_id)
            login_user(user)
            return redirect('/home')
        else:
            return '<h1>invalid credentials!</h1>'
    return render_template('login.html')

@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@login.route('/register_user')
@login_required
def register_user():
    return render_template("register_user.html")

@login.route('/add_user', methods=['GET','POST'])
@login_required
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        users[user] = password
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
        if user and password:
            users[user] = password
    return render_template("users.html", devices=users)

@login.route('/list_users')
@login_required
def list_users():
    global users
    return render_template("users.html", devices=users)

@login.route('/remove_user')
@login_required
def remove_user():
    return render_template("remove_users.html", devices=users)

@login.route('/del_user', methods=['GET','POST'])
@login_required
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        if user:
            users.pop(user, None)
    else:
        user = request.args.get('user', None)
        if user:
            users.pop(user)
    return render_template("users.html", devices=users)
