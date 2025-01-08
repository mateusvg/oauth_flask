from flask import Flask, request, jsonify
from authlib.integrations.flask_oauth2 import AuthorizationServer, ResourceProtector
from authlib.oauth2.rfc6749 import OAuth2Error
from werkzeug.security import gen_salt

# Criando o aplicativo Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['OAUTH2_CLIENTS'] = {
    'client_id': 'client_key',
    'client_secret': 'client_secret'
}

# Iniciar o Authorization Server
authorization = AuthorizationServer(app)

# Protector de recursos
require_oauth = ResourceProtector()

# Função para autenticação do cliente (verificação de client_id e client_secret)
def authenticate_client(client_id, client_secret):
    if client_id == app.config['OAUTH2_CLIENTS']['client_id'] and client_secret == app.config['OAUTH2_CLIENTS']['client_secret']:
        return True
    return False

# Função para gerenciar o token de acesso
@app.route('/token', methods=['POST'])
def issue_token():
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    # Verifica se o cliente foi autenticado
    if not authenticate_client(client_id, client_secret):
        return jsonify({'error': 'Unauthorized'}), 401

    # Emite o token de acesso
    token = gen_salt(32)  # Um token simples para a demonstração
    return jsonify({'access_token': token, 'token_type': 'bearer'}), 200

# Recurso protegido que requer OAuth 2.0
@app.route('/api/protected', methods=['GET'])
@require_oauth('profile')
def protected_resource():
    return jsonify({'message': 'Você acessou um recurso protegido'}), 200

if __name__ == '__main__':
    app.run(debug=True)
