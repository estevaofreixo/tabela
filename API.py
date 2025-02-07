from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    entrada = data.get("input", "")
    resposta = f"Você digitou: {entrada}"  # Aqui você pode conectar com uma IA real
    return jsonify({"output": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
