import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
MODEL = "deepseek-chat"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'no message provided'}), 400

    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        return jsonify({'error': 'server misconfiguration: API key not set'}), 500

    payload = {
        'model': MODEL,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': user_message}
        ],
        'temperature': 0.7,
        'max_tokens': 2048
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    resp = requests.post(DEEPEEK_API_URL, json=payload, headers=headers)
    if not resp.ok:
        return jsonify({'error': 'api request failed', 'detail': resp.text}), resp.status_code

    result = resp.json()
    answer = result.get('choices', [{}])[0].get('message', {}).get('content')
    return jsonify({'reply': answer})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
