import os
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok"), 200

    @app.get("/failcheck")
    def failcheck():
        # Simulate liveness failure when env var is set (used later with livenessProbe)
        should_fail = os.getenv("FAILCHECK", "false").lower() in ("1", "true", "yes")
        return (jsonify(status="fail"), 500) if should_fail else (jsonify(status="ok"), 200)

    @app.get("/")
    def index():
        return jsonify(app="flask-sample", message="hello"), 200

    return app

# Dev-only entrypoint
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
