from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('marks.html')


@app.route('/result/<int:marks>')
def result(marks):
    return render_template('result.html', marks=marks)


@app.route('/marks', methods=['POST'])
def enter_marks():
    marks = request.form['marks']
    return redirect(url_for('result', marks=marks))


@app.route('/result')
def all_result():
    dict = {'PHY': 50, 'CHE': 60, 'MATHS': 70}
    return render_template('all_result.html', result=dict)


if __name__ == '__main__':
    app.run(debug=True)
