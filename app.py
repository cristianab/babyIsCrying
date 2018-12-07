from flask import Flask
import firebase
from firebase import firebase

firebase = firebase.FirebaseApplication('https://babyiscrying-58c27.firebaseio.com/', None)
result = firebase.get('/users', None)

app = Flask(__name__)

@app.route("/")
def main():
    return result

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=80)
