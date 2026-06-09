"""
Flask application entry point.

Run with:
    cd backend
    python app.py

The server will start at http://localhost:5000
"""

from flask import Flask, jsonify
from flask_cors import CORS
from config import DEBUG, SECRET_KEY
from database import init_db
from routes import trainer_bp, battle_bp, pokemon_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

# Allow the frontend (served on a different port) to call our API
CORS(app)

# Register all route blueprints
app.register_blueprint(trainer_bp)
app.register_blueprint(battle_bp)
app.register_blueprint(pokemon_bp)


@app.route("/api/health")
def health():
    """Quick endpoint to check the server is up."""
    return jsonify({"status": "ok"})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": str(e)}), 400


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Create all DB tables on first run
    init_db()
    print("Database initialised.")
    print("Server starting at http://localhost:5000")
    app.run(debug=DEBUG, port=5000)
