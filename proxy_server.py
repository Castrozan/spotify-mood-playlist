import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    try:
        data = request.json
        
        # Make the request to the actual API
        response = requests.post(
            'https://www.taranify.com/api/events',
            headers={
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Origin': 'https://www.taranify.com',
                'Referer': 'https://www.taranify.com/what-to-listen-spotify',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
            },
            json=data
        )
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'API request failed'}), response.status_code
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

