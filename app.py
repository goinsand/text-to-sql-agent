# ===============================
# app.py
# ===============================
from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import agent

app = Flask(__name__)
CORS(app)  # enable CORS for frontend dev

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Missing "question" field'}), 400

    result = agent(question)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

