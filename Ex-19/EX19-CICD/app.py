from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>EX19 CI/CD</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .card {
                text-align: center;
                padding: 50px;
                border-radius: 25px;
                background: rgba(255,255,255,0.15);
                box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            }

            h1 {
                font-size: 42px;
            }

            p {
                font-size: 20px;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🚀 EX19 CI/CD Pipeline</h1>
            <p>GitHub Actions + Docker</p>
            <p>Continuous Deployment Ready ✅</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)