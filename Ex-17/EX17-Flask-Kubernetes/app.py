from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, Flask API is running!"

# Sample API endpoint
@app.route('/api/data')
def get_data():
    data = {
        "name": "Dharani",
        "project": "Flask Kubernetes API",
        "status": "Running Successfully"
    }
    return jsonify(data)

# Health check (important for Kubernetes)
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)