from flask import Flask, request, jsonify
from authlib.integrations.flask_oauth2 import AuthorizationServer
from authlib.oauth2.rfc6749 import grants
from authlib.common.security import generate_token


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta'
app.config['OAUTH2_PROVIDER_TOKEN_EXPIRES_IN'] = 3600  # Token válido por 1 hora

# Inicializa o AuthorizationServer
authorization = AuthorizationServer(app)

# Dados fictícios para OAuth2
CLIENTS = {
    "client_key": {
        "client_id": "client_key",
        "client_secret": "example_client_secret",
        "base_url": "https://seu-conector-de-pagamento.com"
    }
}

# Token de acesso fictício para teste
ACCESS_TOKENS = {}

# Definindo a classe Client
class Client:
    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url

    def check_client_secret(self, client_secret):
        return self.client_secret == client_secret
    
    def check_endpoint_auth_method(self, method, endpoint):
        # Verifica se o método de autenticação é "client_secret_basic"
        if method == 'client_secret_basic':
            return True
        return False

# Instanciando clientes reais
clients = {
    "client_key": Client(
        client_id="client_key",
        client_secret="example_client_secret",
        base_url="https://seu-conector-de-pagamento.com"
    )
}

class ClientCredentialsGrant(grants.ClientCredentialsGrant):
    def authenticate_client(self, client_id, client_secret):
        client = clients.get(client_id)
        if client and client.check_client_secret(client_secret):
            return client

    def create_access_token(self, token, client, grant_user):
        # Salva o token gerado para validação futura
        ACCESS_TOKENS[client.client_id] = token['access_token']
        return token


# Registra o grant type
authorization.register_grant(ClientCredentialsGrant)

# Função para consultar o cliente
def query_client(client_id):
    client_data = CLIENTS.get(client_id)
    if client_data:
        return Client(client_data["client_id"], client_data["client_secret"], client_data["base_url"])
    return None

# Configura o AuthorizationServer para usar o query_client
authorization.query_client = query_client


@app.route('/oauth/token', methods=['POST'])
def generate_token():
    """Endpoint para geração de tokens OAuth2."""
    return authorization.create_token_response()


@app.route('/payment', methods=['POST'])
def process_payment():
    """Endpoint para processar pagamentos."""
    token = request.headers.get('Authorization')
    if not token or token.split()[1] not in ACCESS_TOKENS.values():
        return jsonify({'error': 'unauthorized'}), 401

    payment_data = request.json
    if not payment_data or 'amount' not in payment_data:
        return jsonify({'error': 'invalid_data'}), 400

    # Processa o pagamento (simulação)
    return jsonify({
        'status': 'success',
        'message': f"Pagamento de {payment_data['amount']} processado com sucesso."
    })


@app.route('/payment/connector', methods=['POST'])
def onboard_connector():
    """Endpoint para cadastro de conectores de pagamento.""" 
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
