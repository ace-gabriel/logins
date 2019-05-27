from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os

app = Flask(__name__)

@app.route("/home", methods=['POST', 'GET'])
def main():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('logged_in.html')

@app.route('/login', methods=['POST', 'GET'])
def admin_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['logged_in'] = True
        return redirect(url_for('main'))
    else:
        flash("Invalid credentials. Please try again")
        return render_template('login.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
