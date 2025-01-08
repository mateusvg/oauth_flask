from flask import Flask, request, jsonify
from werkzeug.utils import cached_property
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta'
app.config['OAUTH2_PROVIDER_TOKEN_EXPIRES_IN'] = 3600  # Token válido por 1 hora

# Inicializa o provedor OAuth2
oauth = OAuth2Provider(app)

# Dados fictícios para OAuth2
CLIENTS = {
    "client_key": "example_client_key",
    "client_secret": "example_client_secret",
    "base_url": "https://seu-conector-de-pagamento.com"
}

# Token de acesso fictício para teste
ACCESS_TOKENS = {}


@app.route('/oauth/token', methods=['POST'])
def generate_token():
    """Rota para gerar o token de acesso OAuth2"""
    client_key = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    if client_key == CLIENTS['client_key'] and client_secret == CLIENTS['client_secret']:
        # Gera um token simples
        access_token = 'token_simulado_123456'
        ACCESS_TOKENS[client_key] = access_token
        return jsonify({
            'access_token': access_token,
            'token_type': 'Bearer',
            'expires_in': app.config['OAUTH2_PROVIDER_TOKEN_EXPIRES_IN']
        })
    return jsonify({'error': 'invalid_client'}), 401


@app.route('/payment', methods=['POST'])
def process_payment():
    """Rota para receber os dados de pagamento"""
    token = request.headers.get('Authorization')
    if not token or token.split()[1] not in ACCESS_TOKENS.values():
        return jsonify({'error': 'unauthorized'}), 401

    payment_data = request.json
    # Valida os dados recebidos
    if not payment_data or 'amount' not in payment_data:
        return jsonify({'error': 'invalid_data'}), 400

    # Processa o pagamento (simulação)
    return jsonify({
        'status': 'success',
        'message': f"Pagamento de {payment_data['amount']} processado com sucesso."
    })


@app.route('/payment/connector', methods=['POST'])
def onboard_connector():
    """Rota para cadastrar um novo conector de pagamento"""
    data = request.json
    required_fields = ['payment_connector_name', 'base_url', 'client_key', 'client_secret']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'missing_fields'}), 400

    # Salva o conector no banco (simulação)
    connector_data = {
        'name': data['payment_connector_name'],
        'base_url': data['base_url'],
        'client_key': data['client_key'],
        'client_secret': data['client_secret']
    }
    return jsonify({
        'status': 'success',
        'message': 'Conector cadastrado com sucesso.',
        'connector': connector_data
    })


if __name__ == '__main__':
    app.run(debug=True)
