#ms23svr

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'simon': 3}

@app.route('/players')
def players():
    return {'player1':  1, 'player2': 2, 'player3': 3}