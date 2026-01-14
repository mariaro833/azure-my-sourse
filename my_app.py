from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    # For local development
    app.run(debug=True)
else:
    # For production (Azure/Gunicorn)
    port = int(os.environ.get('PORT', 8000))