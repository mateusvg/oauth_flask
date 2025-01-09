from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

# Variáveis de configuração (ajustadas com os seus dados)
OAUTH_URL = "https://github.com/login/oauth/access_token"  # URL para obter o token do GitHub
CLIENT_ID = "Ov23liBQqZ86S7yMjC2A"  # Seu client_id do GitHub
CLIENT_SECRET = "29f28cf34a9c06b2e8d1cc74679e6f7b2a58399b"  # Seu client_secret do GitHub
SCOPE = "repo"  # Defina o escopo conforme necessário (exemplo: 'repo' para acessar repositórios)
REDIRECT_URI = "http://oauth-flask.onrender.com/callback"  # URL de redirecionamento após autenticação

# URL do provedor OAuth (GitHub)
AUTH_URL = "https://github.com/login/oauth/authorize"  # URL de autorização do GitHub

@app.route('/login', methods=['GET'])
def login():
    # Construindo a URL de autorização para o GitHub
    authorization_url = f"{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}&response_type=code"
    return redirect(authorization_url)


@app.route('/callback', methods=['GET'])
def callback():
    # O GitHub redireciona para cá com o código de autorização
    code = request.args.get('code')
    
    if not code:
        return jsonify({
            'status': 'error',
            'message': 'Authorization code missing'
        }), 400

    # Dados para obter o token OAuth usando o código de autorização
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code
    }

    try:
        # Fazendo a requisição para o servidor OAuth (GitHub) para trocar o código por um token
        response = requests.post(OAUTH_URL, data=data, headers={'Accept': 'application/json'})

        if response.status_code == 200:
            token = response.json().get('access_token')
            return jsonify({
                'status': 'success',
                'access_token': token
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to fetch the token',
                'details': response.json()
            }), response.status_code

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
