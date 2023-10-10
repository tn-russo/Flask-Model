from flask import Flask

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return "Teste FlaskPython"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
