import logging
from flask import Flask, request, jsonify

# Configuração do logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Configura o log para capturar tudo
app = Flask(__name__)

@app.before_request
def log_request_info():
    # Loga todos os detalhes da requisição antes de processá-la
    logger.debug(f'Requisição recebida: {request.method} {request.url}')
    logger.debug(f'Cabeçalhos: {request.headers}')
    if request.data:
        logger.debug(f'Dados recebidos: {request.data}')

@app.after_request
def log_response_info(response):
    # Loga todos os detalhes da resposta após processá-la
    logger.debug(f'Resposta enviada: {response.status}')
    logger.debug(f'Cabeçalhos da resposta: {response.headers}')
    return response

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()  # Pega os dados JSON do corpo da requisição
    if data:
        logger.info(f'Dados recebidos: {data}')
        return jsonify({"message": "Dados recebidos", "data": data}), 200
    else:
        logger.warning(f'Erro: Nenhum dado enviado. Dados recebidos: {request.data}')
        return jsonify({"message": "Nenhum dado enviado"}), 400

if __name__ == '__main__':
    app.run(debug=True)
