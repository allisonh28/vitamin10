from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/quote')
def get_quote():
    try:
        response = requests.get("https://dummyjson.com/quotes/random")
        data = response.json()
        return jsonify({
            'quote': data.get('quote'),
            'author': data.get('author')
        })
    except Exception as e:
        return jsonify({'error': 'Failed to fetch quote', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
