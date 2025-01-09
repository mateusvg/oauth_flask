from flask import Flask, request, jsonify

app = Flask(__name__)

# Função fictícia para validar o token
def validate_oauth_token(token):
    # Aqui você poderia validar o token com um provedor externo (ex.: Google, Auth0)
    # ou verificar um banco de dados local. No exemplo, vamos validar tokens específicos.
    valid_tokens = {"valid_token_123", "valid_token_456"}  # Tokens de exemplo
    return token in valid_tokens

@app.route('/verify-token', methods=['POST'])
def verify_token():
    # Obtém o cabeçalho Authorization
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        return jsonify({"error": "Authorization header is missing"}), 401

    # Verifica o formato do cabeçalho
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Invalid Authorization header format"}), 400

    # Extrai o token do cabeçalho
    token = auth_header.split(" ")[1]

    # Valida o token
    if validate_oauth_token(token):
        return jsonify({"message": "Token is valid"}), 200
    else:
        return jsonify({"error": "Invalid token"}), 401

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
