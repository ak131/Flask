from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('user.html')


@app.route('/set_cookie', methods=['POST', 'GET'])
def set_cookie():
    user = request.form['User']
    resp = make_response(render_template('read_cookie.html', user_id=user))
    resp.set_cookie('userID', user)

    return resp


@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome ' + name + '</h1>'


if __name__ == '__main__':
    app.run(debug=True)