"""
in this project I built an API for movie lines 
currently, there are 2 endpoints, first one is ../api/v1.0/randomlines
and the second endpoint is /api/v1.0/famousquotes
the first endpoint picks a movie line between more than 450.000 lines and returns it. 
The second endpoint is returning a famous quote form known movies 
API lives in the http://randommovielines.herokuapp.com/ URL 
you can visit the desired endpoint and explore the API 

for more information and contact you can check out my GitHub profile
GitHub : https://github.com/YigitGunduc

This project is licensed under the MIT License (see the LICENSE file for details).
"""
import os
import random
from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)
dirname = os.path.dirname(__file__)
movie_lines = os.path.join(dirname, 'movie_lines.txt')
famous_quotes = os.path.join(dirname, 'famousquotes.txt')

lines = open(movie_lines).read().split("\n")
famous_lines = open(famous_quotes).read().split("\n")

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the movies API for more information and endpoints you can check out the GitHub link https://github.com/YigitGunduc/Random-Movie-Lines"

@app.route('/api/v1.0/randomlines', methods=['GET'])
def random_line():
    randomLine = random.choice(lines)
    return jsonify({'line': randomLine})

@app.route('/api/v1.0/famousquotes', methods=['GET'])
def famous_line():
    randomLine = random.choice(famous_lines)
    return jsonify({'quote': randomLine})

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    
