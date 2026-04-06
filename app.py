from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deployed System</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', sans-serif;
            }

            body {
                overflow-x: hidden;
                background: black;
                color: white;
            }

            section {
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 20px;
            }

            .hero {
                background: linear-gradient(120deg, #000000, #1a1a2e, #16213e);
                animation: fadeIn 2s ease-in;
            }

            .hero h1 {
                font-size: 60px;
                letter-spacing: 2px;
                text-shadow: 0 0 20px rgba(0,255,255,0.7);
            }

            .hero p {
                margin-top: 20px;
                font-size: 20px;
                opacity: 0.8;
            }

            .section2 {
                background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
            }

            .section3 {
                background: linear-gradient(120deg, #141e30, #243b55);
            }

            .card {
                background: rgba(255,255,255,0.05);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 40px rgba(0,255,255,0.2);
                transition: transform 0.5s ease;
            }

            .card:hover {
                transform: scale(1.05);
            }

            h2 {
                font-size: 40px;
                margin-bottom: 20px;
            }

            p {
                font-size: 18px;
                opacity: 0.8;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .scroll {
                position: absolute;
                bottom: 20px;
                font-size: 14px;
                opacity: 0.6;
                animation: bounce 2s infinite;
            }

            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(10px); }
            }
        </style>
    </head>
    <body>

        <section class="hero">
            <div>
                <h1>DEPLOYED</h1>
                <p>Continuous Integration • Continuous Delivery</p>
                <div class="scroll">Scroll ↓</div>
            </div>
        </section>

        <section class="section2">
            <div class="card">
                <h2>Automation</h2>
                <p>Code moves seamlessly from commit to deployment without manual intervention.</p>
            </div>
        </section>

        <section class="section3">
            <div class="card">
                <h2>Scalability</h2>
                <p>Built on cloud infrastructure, designed to scale and adapt dynamically.</p>
            </div>
        </section>

        <section class="section2">
            <div class="card">
                <h2>Reliability</h2>
                <p>Automated workflows ensure consistent and repeatable deployments.</p>
            </div>
        </section>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
