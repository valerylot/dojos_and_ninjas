from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo


@app.route('/dojos')
def dashboard():
    dojos = Dojo.get_dojos()
    print(dojos)
    return render_template('dojos.html', all_dojos = dojos)

@app.route('/dojos/create', methods=["POST"])
def new_dojo():
    Dojo.save(request.form)
    print(request.form)
    return redirect ('/dojos')


