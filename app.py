 
from flask import Flask, render_template, request
from calculadora import suma, resta, multiplicacion, division

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operacion = request.form["operacion"]
        if operacion == "suma":
            resultado = suma(a, b)
        elif operacion == "resta":
            resultado = resta(a, b)
        elif operacion == "multiplicacion":
            resultado = multiplicacion(a, b)
        elif operacion == "division":
            try:
                resultado = division(a, b)
            except ValueError as e:
                resultado = str(e)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)