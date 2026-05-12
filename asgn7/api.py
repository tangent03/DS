from flask import Flask, request, jsonify

app = Flask(__name__)


def get_numbers():

    data = request.get_json()

    try:

        num1 = float(data["num1"])
        num2 = float(data["num2"])

        return num1, num2

    except:

        return None, None


@app.route("/<operation>", methods=["POST"])
def calculate(operation):

    num1, num2 = get_numbers()

    if num1 is None:

        return jsonify(error="Invalid input")

    if operation == "add":

        result = num1 + num2

    elif operation == "subtract":

        result = num1 - num2

    elif operation == "multiply":

        result = num1 * num2

    elif operation == "divide":

        if num2 == 0:

            return jsonify(error="Cannot divide by zero")

        result = num1 / num2

    else:

        return jsonify(error="Invalid operation")

    return jsonify(result=result)


if __name__ == "__main__":

    print("\nAPI Running on:")
    print("http://127.0.0.1:5000\n")

    app.run(debug=True)