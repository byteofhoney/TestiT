from flask import Flask
from flask_cors import CORS
from config import SECRET_KEY
from db import db

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
CORS(app)

@app.route("/health")
def health():
    try:
        db.command("ping")
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {"status": "ok", "service": "testit-api", "database": db_status}

if __name__ == "__main__":
    app.run(debug=True)