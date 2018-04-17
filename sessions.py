from flask import Flask, session, render_template, request, redirect, url_for
app = Flask(__name__)

# Must add secret key for session
app.secret_key = 'ABC'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('session_welcome.html', username=username)
    return render_template('session_error.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['user']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
