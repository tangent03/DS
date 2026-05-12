from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = request.form["operation"]

    payload = {
        "num1": num1,
        "num2": num2
    }

    url = f"http://127.0.0.1:5000/{operation}"

    response = requests.post(url, json=payload)

    result = response.json()

    return render_template("index.html", result=result)


if __name__ == "__main__":

    print("\nOpen Calculator:")
    print("http://127.0.0.1:3000\n")

    app.run(debug=True, port=3000)