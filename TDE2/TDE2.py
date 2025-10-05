from flask import Flask, render_template
from login import login
from sensores import sensors
from atuadores import actuators
from flask_login import LoginManager
from login import login, User

app= Flask(__name__)
app.secret_key = 'rayssa-gaievicz-grafetti'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.validated_user' # type: ignore

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/')
def sensores():
    return render_template('sensor.html')

@app.route('/')
def atuadores():
    return render_template('atuador.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
