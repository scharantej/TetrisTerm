
# main.py - Flask application for Tetris

from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Game state
board = [[' ' for _ in range(10)] for _ in range(20)]
current_tetromino = [[random.choice('OIZLJS') for _ in range(4)] for _ in range(4)]
current_x = 4
current_y = 0
score = 0

# Routes
@app.route('/')
def index():
    return render_template('index.html', board=board, current_tetromino=current_tetromino, score=score)

@app.route('/move')
def move():
    global current_x, current_y
    direction = request.args.get('direction')
    if direction == 'left' and current_x > 0:
        current_x -= 1
    elif direction == 'right' and current_x < 9:
        current_x += 1
    return index()

@app.route('/rotate')
def rotate():
    global current_tetromino
    current_tetromino = list(zip(*current_tetromino[::-1]))
    return index()

@app.route('/game_over')
def game_over():
    return render_template('game_over.html')

if __name__ == '__main__':
    app.run()
