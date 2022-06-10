import math

from flask import Flask, render_template, request

from utils import find_roots, guess_the_color_from_the_number

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find_roots')
def form_factors():
    return render_template('find_roots.html')


@app.route('/find_roots', methods=['POST'])
def post_factors():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    return find_roots(a, b, c)


@app.route('/guess_color')
def guess_color():
    return render_template('guess_the_color.html')


@app.route('/guess_color', methods=['POST'])
def post_guess_color():
    number = request.form['number']
    if not number.isdigit():
        return "Введенное значение должны быть числом"
    return str(guess_the_color_from_the_number(int(number)))


if __name__ == '__main__':
    app.run()
