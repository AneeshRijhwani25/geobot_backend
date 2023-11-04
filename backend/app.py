from flask import Flask, request, jsonify
from model import categorize_entities

app = Flask(__name__)

@app.route('/api/categorize', methods=['POST'])
def categorize():
    try:
        data = request.get_json()
        text = data['text']
        categorized = categorize_entities(text)
        return jsonify(categorized)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
