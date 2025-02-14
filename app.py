from flask import Flask, render_template, request
from sympy import symbols, Eq, solve, simplify, diff, integrate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Ambil input dari form
        equation = request.form.get('equation')
        operation = request.form.get('operation')

        try:
            x = symbols('x')  # Mendefinisikan simbol x

            if operation == 'solve':
                # Memecahkan persamaan
                eq = Eq(eval(equation), 0)
                result = solve(eq, x)
            elif operation == 'simplify':
                # Menyederhanakan ekspresi
                result = simplify(equation)
            elif operation == 'differentiate':
                # Menghitung turunan
                result = diff(equation, x)
            elif operation == 'integrate':
                # Menghitung integral
                result = integrate(equation, x)
            else:
                result = "Operasi tidak valid."
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)