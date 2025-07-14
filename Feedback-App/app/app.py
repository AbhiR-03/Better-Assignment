from flask import Flask, request, jsonify

app = Flask(__name__)
feedbacks = []

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    feedbacks.append(data)
    return jsonify({"message": "Feedback received!"}), 201

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify(feedbacks), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
