from flask import Blueprint, request, render_template
from flask_login import login_required

sensors = Blueprint("sensors", __name__ , template_folder="templates")

sensores = {
    'Umidade':22,
    'Temperatura':23,
    'Luminosidade':1034
}

@sensors.route('/register_sensor')
@login_required
def register_sensor():
    return render_template("register_sensor.html")
@sensors.route('/add_sensor', methods=['GET','POST'])
@login_required
def add_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        valor = request.form['valor']
        valor = int(request.form['valor'])
        sensores[sensor] = valor
    else:
        sensor = request.args.get('sensor', None)
        valor = request.args.get('valor', None)
        if sensor and valor:
            valor = int(request.form['valor'])
            sensores[sensor] = int(valor)
    return render_template("sensor.html", sensores=sensores)

@sensors.route('/remove_sensor')
@login_required
def remove_sensor():
    return render_template("remove_sensores.html", sensores=sensores)
@sensors.route('/del_sensor', methods=['GET','POST'])
@login_required
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        if sensor:
            sensores.pop(sensor, None)
    else:
        sensor = request.args.get('sensor', None)
        if sensor:
            sensores.pop(sensor)
    return render_template("sensor.html", sensores=sensores)

@sensors.route('/list_sensores')
@login_required
def sensor():
    global sensores
    return render_template("sensor.html", sensores=sensores)
