from flask import render_template, flash, redirect, url_for, request
from app import app, functions
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Friend'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('User {} successfully logged in, remember_me = {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)







@app.route('/schedule')
def schedule():
   rows = functions.get_from_db()
   return render_template('schedule.html', rows = rows)

@app.route('/addrec',methods = ['POST', 'GET'])
def input_rows():
    msg = functions.input_in_db()
    return render_template("result.html",msg = msg)


@app.route('/list')
def list():
    rows = functions.get_from_db()
    return render_template("list.html",rows = rows)
