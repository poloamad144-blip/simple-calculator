
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    try:
        a = float(data["a"])
        b = float(data["b"])
        operation = data["operation"]

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                return jsonify({"error": "مينفعش القسمة على صفر"}), 400
            result = a / b
        else:
            return jsonify({"error": "عملية غير صحيحة"}), 400

        if not (abs(result) < float("inf")):
            return jsonify({"error": "النتيجة خارج النطاق"}), 400

        return jsonify({"result": result})

    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "من فضلك أدخل أرقام صحيحة"}), 400

if __name__ == "__main__":
    app.run(debug=True)
