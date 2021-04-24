from flask import Flask
# https://realpython-example-app-atrifa.herokuapp.com/
app = Flask(__name__)


@app.route("/")
def index():
    return "This is yet another version"


if __name__ == "__name__":
    print('end script')
