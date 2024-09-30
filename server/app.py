from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Return to browser

@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a string with numbers from 0 to parameter-1, each on a new line
    count_str = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return count_str

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation', 400

if __name__ == '__main__':
    app.run(debug=True, port=5555)
