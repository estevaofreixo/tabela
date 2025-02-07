import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API está rodando!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    entrada = data.get("input", "")
    resposta = f"Você digitou: {entrada}"
    return jsonify({"output": resposta})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa a porta do Render
    app.run(host="0.0.0.0", port=port)
