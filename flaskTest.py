#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, render_template, request
from connect4 import Connect4

app = Flask(__name__)

game=Connect4()

@app.route('/')
def index(board=game.stringify()):
	return render_template('index.html',board=board)

@app.route('/move',methods=['POST'])
def move():
    print (request, request.data, request.content_type)
    data=request.get_json()
    print (data)
    print ("Hello")
    move=data['column']
    game.make_move(move)
    return game.stringify()

@app.route('/restart',methods=['POST'])
def restart():
	game.__init__()
	return game.stringify()

if __name__=="__main__":
	app.run(debug=True)