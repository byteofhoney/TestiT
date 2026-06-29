from flask import Flask
from flask_cors import CORS
from config import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
CORS(app)

@app.route("/health")
def health():
    return {"status": "ok", "service": "testit-api"}

if __name__ == "__main__":
    app.run(debug=True)