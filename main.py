import flask

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def returnAlways():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, port=5000)