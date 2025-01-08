from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()  # Pega os dados JSON do corpo da requisição
    if data:
        return jsonify({"message": "Dados recebidos", "data": data}), 200
    else:
        return jsonify({"message": "Nenhum dado enviado"}), 400

if __name__ == '__main__':
    app.run(debug=True)
