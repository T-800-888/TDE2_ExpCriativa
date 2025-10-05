from flask import Blueprint, request, render_template
from flask_login import login_required

actuators = Blueprint("actuator", __name__ , template_folder="templates")

atuadores = [
    'Motores elétricos',
    'Válvulas rotativas',
    'Garras manipuladoras'
]

@actuators.route('/register_atuador')
@login_required
def register_atuador():
    return render_template("register_atuador.html")
@actuators.route('/add_atuador', methods=['GET','POST'])
@login_required
def add_atuador():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        if atuador:  # só adiciona se não for vazio
            atuadores.append(atuador)
    else:
        atuador = request.args.get('atuador', None)
        if atuador:  # só adiciona se não for vazio
            atuadores.append(atuador)
    return render_template("atuador.html", atuadores=atuadores)

@actuators.route('/list_atuadores')
@login_required
def atuador():
    global atuadores
    return render_template("atuador.html", atuadores=atuadores)

@actuators.route('/remove_atuador')
@login_required
def remove_atuador():
    return render_template("remove_atuadores.html", atuadores=atuadores)
@actuators.route('/del_atuador', methods=['GET','POST'])
@login_required
def del_atuador():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        if atuador:
            atuadores.remove(atuador)
    else:
        atuador = request.args.get('atuador', None)
        if atuador:
            atuadores.remove(atuador)
    return render_template("atuador.html", atuadores=atuadores)
