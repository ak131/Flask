from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


# URL
@app.route('/page')
def welcome_page():
    return "Welcome"

# This method is not working
def second_page():
    return "Second Page!"
app.add_url_rule('/', 'second', second_page)


# Dynamic URL (rule using string)
@app.route('/hello/<name>')
def hello_param(name):
    return "Hello {}!".format(name)


# Dynamic URL (rule using int)
@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return "Post id is '{}'".format(post_id)


# Dynamic URL (rule using float)
@app.route('/site/<float:ver_no>')
def show_version(ver_no):
    return "Version No. is %0.3f" % ver_no


# Canonical rule using '/', '/flask' and '/flask/' will be same.
@app.route('/flask/')
def hello_python():
    return "Hello Flask!"


if __name__ == '__main__':
    app.run(debug=True)
