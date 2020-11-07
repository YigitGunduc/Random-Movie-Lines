"""
in this project I built an API for movie lines 
currently, there are 2 endpoints, first one is ../api/v1.0/randomlines
and the second endpoint is /api/v1.0/famousquotes
the first endpoint picks a movie line between more than 450.000 lines and returns it. 
The second endpoint is returning a famous quote form known movies 
API lives in the http://randommovielines.herokuapp.com/ URL 
you can visit the desired endpoint and explore the API 

for more information and contact check out GitHub page
GitHub : https://github.com/YigitGunduc

This project is licensed under the MIT License (see the LICENSE file for details).
"""
import os
import random
from flask import Flask, jsonify, render_template
from waitress import serve

app = Flask(__name__)
dirname = os.path.dirname(__file__)
movie_lines = os.path.join(dirname, 'movie_lines.txt')
famous_quotes = os.path.join(dirname, 'famousquotes.txt')

lines = open(movie_lines).read().split("\n")
famous_lines = open(famous_quotes).read().split("\n")

@app.route('/', methods=['GET'])
def index(): 
    randomLine = random.choice(lines)
    famousLine = random.choice(famous_lines)
    return render_template('index.html')

@app.route('/famousquotes', methods=['GET'])
def famousquotes(): 
    famousLine = random.choice(famous_lines)
    return render_template('famous.html', famousLine=famousLine)

@app.route('/randomlines', methods=['GET'])
def randomLine(): 
    randomLine = random.choice(lines)
    return render_template('randomline.html', randomLine=randomLine)

@app.route('/api/v1.0/randomlines', methods=['GET'])
def random_line():
    randomLine = random.choice(lines)
    return jsonify({'line': randomLine})

@app.route('/api/v1.0/famousquotes', methods=['GET'])
def famous_line():
    randomLine = random.choice(famous_lines)
    return jsonify({'quote': randomLine})

if __name__ == '__main__':
    app.run(debug=True)
    #serve(app, host="0.0.0.0", port=8080)
    

