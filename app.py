import os
import random
from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'movie_lines.txt')

lines = open(filename).read().split("\n")

@app.route('/api/v1.0/randomlines', methods=['GET'])
def get_line():
    randomLine = random.choice(lines)
    return jsonify({'line': randomLine})


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    