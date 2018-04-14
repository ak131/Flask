from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    html = '<html>' \
           '<head><title>Welcome</title></head>' \
           '<body><h1>Hello World!</h1></body></html>'
    return html


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
