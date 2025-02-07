from flask import Flask, render_template, jsonify, request
import random, json, os, threading, time

app = Flask(__name__)
SCORES_FILE = "player_scores.json"

questions_pool = [
    {"question": "What year was Amazon founded?", "answer": "1994"},
    {"question": "Who is the CEO of Amazon?", "answer": "andy jassy"},
    {"question": "What is the name of Amazon's voice assistant?", "answer": "alexa"},
    {"question": "What is Amazon's cloud computing service called?", "answer": "aws"},
    {"question": "Where is Amazon's headquarters located?", "answer": "seattle"},
    {"question": "What was Amazon originally known for selling?", "answer": "books"},
    {"question": "What is the name of Amazon's video streaming service?", "answer": "prime video"},
    {"question": "What is Amazon's AI chatbot for customer service?", "answer": "amazon q"},
    {"question": "Which Amazon device helps control smart home devices?", "answer": "echo"},
    {"question": "What is the name of Amazon's cashier-less stores?", "answer": "amazon go"},
    {"question": "Which day is Amazon's biggest annual sales event?", "answer": "prime day"},
    {"question": "Which company did Amazon acquire in 2017 for $13.7 billion?", "answer": "whole foods"},
    {"question": "What is the main color of Amazon's logo?", "answer": "Orange"},
    {"question": "What is the name of Amazon's AI-powered recommendation algorithm?", "answer": "a9"},
    {"question": "Which day is Amazon's biggest annual sales event?", "answer": "prime day"},
    {"question": "What is the name of Amazon's charity donation program?", "answer": "smile"},
    {"question": "What is the name of Amazon's online game streaming platform?", "answer": "twitch"},
    {"question": "Which Amazon warehouse robotics company was acquired in 2012?", "answer": "kiva"},
    
]

def get_random_questions():
    return random.sample(questions_pool, 5)  # Select 5 unique questions per game

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    return []

def save_scores(scores):
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_questions')
def get_questions():
    return jsonify(get_random_questions())

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    username, score = data['username'], data['score']
    scores = load_scores()
    scores.append({"username": username, "score": score})
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    save_scores(scores)
    return jsonify({"message": "Score saved successfully", "scores": scores})

@app.route('/get_scores')
def get_scores():
    return jsonify(load_scores())

if __name__ == '__main__':
    app.run(debug=True)
