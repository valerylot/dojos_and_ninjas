from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {"id" : id}
    return render_template('show.html', data = data, dojos = Dojo.dojo_ninjas(data))

@app.route('/ninjas')
def add_ninjas():
    dojos = Dojo.get_dojos()
    return render_template('ninjas.html', all_dojos = dojos)

@app.route('/create/ninjas', methods=['POST'])
def create_ninjas():
    Ninja.save(request.form)
    print(request.form)
    return redirect ('/dojos')
