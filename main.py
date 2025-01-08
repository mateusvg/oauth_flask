import logging
from flask import Flask, request, jsonify, Response

# Configuração do logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.before_request
def log_request_info():
    logger.debug(f'Requisição recebida: {request.method} {request.url}')
    logger.debug(f'Cabeçalhos: {request.headers}')
    if request.data:
        logger.debug(f'Dados recebidos: {request.data}')

@app.after_request
def log_response_info(response):
    logger.debug(f'Resposta enviada: {response.status}')
    logger.debug(f'Cabeçalhos da resposta: {response.headers}')
    return response

@app.route('/post', methods=['POST'])
def post_example():
    data = request.form  # Pega os dados do corpo da requisição, assumindo que são enviados como formulário
    if data:
        logger.info(f'Dados recebidos: {data}')
        response = jsonify({"message": "Dados recebidos", "data": data})
        response.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        return response, 200
    else:
        logger.warning(f'Erro: Nenhum dado enviado. Dados recebidos: {request.data}')
        response = jsonify({"message": "Nenhum dado enviado"})
        response.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        return response, 400

if __name__ == '__main__':
    app.run(debug=True)
