from flask import Flask, render_template

app = Flask(__name__)

# Rota da Página Inicial
@app.route('/')
def home():
    # Você pode passar variáveis do Python para o HTML
    dados_psicologa = {
        "nome": "Dra. Alessandra Moreira",
        "crp": "06/12345"
    }
    return render_template('index.html', dados=dados_psicologa)

# Rota Sobre Mim
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)