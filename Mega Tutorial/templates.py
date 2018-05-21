# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    user = {'username': 'Zoro'}
    html = """
    <html>
        <head>
            <title>Homepage - {}</title>
        </head>
        <body>
            <h1>Hello {}!</h1>
        </body>
    </html>
    """.format(user['username'], user['username'])
    return html


@app.route('/user')
def hello_user():
    user = {'username': 'Straw Hat'}
    # return render_template('index.html', title='Home', user=user)
    # return render_template('index.html', user=user)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)