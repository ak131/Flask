# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
