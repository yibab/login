from unicodedata import category
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['Get', 'Post'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up', methods=['Get', 'Post'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName =  request.form.get('firstName')
        password1 = request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error')
        elif len(firstName) < 2:
            flash("First name must be greater than 1 characters.", category='error')
        elif password1 != password2:
            flash("Passwords dont match.", category='error')
        elif len(password1) < 7:
            flash("Password must be atleast 7 characters.", category='error')
        else:
            flash("Account Created!", category='success')
            pass

    return render_template("sign_Up.html")