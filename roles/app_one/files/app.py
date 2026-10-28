from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        app="Application One",
        message="Hello from the Flask app!",
        managed_by="Ansible"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
