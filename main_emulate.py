import flask
from main import heroes

app = flask.Flask('functions')
methods = ['GET', 'POST', 'PUT', 'DELETE']

@app.route('/glossary', methods=methods)
@app.route('/glossary/<path>', methods=methods)
def catch_all(path=''):
    flask.request.path = '/' + path
    return heroes(flask.request)

if __name__ == '__main__':
    app.run()