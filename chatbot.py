from flask import Flask, request, jsonify, render_template
import os
import json
import uuid

# Remove cohere if not installed, or mock it if needed
# import cohere
# cohere.Client("gfhVvOrF8Qh2wCYeMJoYx9per8JKmR3")

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('aec.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question', '')
    answer = get_answer(user_input)
    return jsonify({'answer': answer})

def get_answer(user_input):
    qna = {
        "college name": "Loknayak JaiPrakash Institute of Technology, Chhapra",
        "abbreviated college name": "LNJPIT CHHAPRA",
        "village": "Maha Gaon",
        "locality": "Newaji tola",
        "city": "Chhapra",
        "district": "Saran",
        "subdivision": "Saran",
        "state": "Bihar",
        "country": "India",
        "pincode": "841302",
        "linkedin id": "Training and Placement Cell, LNJPIT",
        "website url": "https://www.lnjpitchapra.in/",
        "campus area": "45 acres",
        "establishment date": "8-9-2012",
        "principal": "Dr. Mithilesh Kumar Singh",
        "google map location": "https://maps.app.goo.gl/omavakJ4aHPr2AkS8",
        "phone number": "9431064610",
        "name": "Dr. Mithilesh Kumar Singh"
    }
    return qna.get(user_input.lower(), "Sorry, I don't understand your question.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
