from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Deployed 🚀</title>
        <style>
            body {
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                font-size: 50px;
                margin-bottom: 10px;
            }
            p {
                font-size: 20px;
                opacity: 0.9;
            }
            .box {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            .emoji {
                font-size: 60px;
            }
            .footer {
                margin-top: 40px;
                font-size: 14px;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>

        <div class="box">
            <div class="emoji">🔥🚀</div>
            <h1>It Works!</h1>
            <p>Your CI/CD pipeline just deployed this app like a boss 😎</p>
            <p>GitHub → EC2 → LIVE 🎯</p>
        </div>

        <div class="footer">
            Built with ❤️ using Flask + GitHub Actions + AWS
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
