import logging
from flask import Flask, request, jsonify

# Configuração do logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()  # Pega os dados JSON do corpo da requisição
    if data:
        return jsonify({"message": "Dados recebidos", "data": data}), 200
    else:
        logger.error("Erro: Nenhum dado enviado. Dados recebidos: %s", request.data)
        return jsonify({"message": "Nenhum dado enviado"}), 400

if __name__ == '__main__':
    app.run(debug=True)
