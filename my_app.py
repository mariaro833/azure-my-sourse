from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Maria's Azure Web Server!\n"

if __name__ == "__main__":
    app.run(debug=True)
