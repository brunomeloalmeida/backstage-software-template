from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'message': 'You are doing great! Keep it up!',
        'deployed_on': 'kubernetes',
        'env': '${{values.app_env}}',
        'app_name': '${{values.app_name}}',
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#'/api/v1/info'
#'/api/v1/healthz'
