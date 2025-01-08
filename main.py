from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return "Bem-vindo à página inicial!"

@app.route('/redirect-to-home', methods=['GET'])
def redirect_to_home():
    return redirect(url_for('home'))  # Redireciona para a rota 'home'

if __name__ == '__main__':
    app.run(debug=True)
