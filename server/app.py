#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:integer>')
def count(integer):
    count_list = []

    for number in range(integer):
        count_list.append(str(number))
    
    return "\n".join(count_list) + "\n"

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    op = False
    if operation == "+":
        op = num1 + num2
    elif operation == "-":
        op = num1 - num2
    elif operation == "div":
        op = num1 / num2
    elif operation == "*":
        op = num1 * num2
    elif operation == '%':
        op = num1 % num2
    return str(op)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
