import flask
from main import mainFunc

app = flask.Flask('functions')
methods = ['GET', 'POST', 'PUT', 'DELETE']

@app.route('/', methods=methods)
@app.route('/<path>', methods=methods)
def catch_all(path=''):
    flask.request.path = '/' + path
    return mainFunc(flask.request)

if __name__ == '__main__':
    app.run()