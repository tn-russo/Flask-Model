from flask import Flask

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return "Teste FlaskPython"

@app.route('/testroute')
def second_route():
    return "Teste 2 com rota"

@app.route('/testerota3')
def second_rooutoute():
    return "Teste 3 com rota"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
