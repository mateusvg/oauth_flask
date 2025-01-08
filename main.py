from flask import Flask, request, jsonify
from authlib.integrations.flask_oauth2 import AuthorizationServer, ResourceProtector
from werkzeug.security import gen_salt
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['OAUTH2_CLIENTS'] = {
    'client_key': 'client_secret'
}

authorization = AuthorizationServer(app)

require_oauth = ResourceProtector()

def authenticate_client(client_id, client_secret):
    """Verifica se o cliente e seu segredo são válidos."""
    if app.config['OAUTH2_CLIENTS'].get(client_id) == client_secret:
        return True
    return False


@app.route('/token', methods=['GET'])
def issue_token():
    """Emite um token de acesso quando o cliente se autentica corretamente."""
    request_data = request.get_data(as_text=True)
    logging.debug(f"Corpo da requisição: {request_data}")
    
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    # Verifica se o cliente foi autenticado
    if not authenticate_client(client_id, client_secret):
        logging.error(f"Falha na autenticação. client_id: {client_id}, client_secret: {client_secret}")
        return jsonify({'error': 'Unauthorized'}), 401

    # Emite o token de acesso
    token = gen_salt(32)  # Um token simples
    return jsonify({'access_token': token, 'token_type': 'bearer'}), 200


# Recurso protegido que requer OAuth 2.0
@app.route('/api/protected', methods=['GET'])
@require_oauth('profile')
def protected_resource():
    """Recurso protegido que exige um token de acesso válido."""
    return jsonify({'message': 'Você acessou um recurso protegido'}), 200


if __name__ == '__main__':
    app.run(debug=True)
