import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    name = 'John'
    age = '73'
    return flask.render_template('index.html', name=name, age=age)


@app.route('/witty')
def create():
    return flask.render_template('makeawitty.html')
app.run(port=5000)