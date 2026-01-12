import os
from flask import Flask, render_template

app = Flask(__name__)

# --- BLOCO DE SEGURANÇA (Radiografia) ---
# Isso vai aparecer nos logs do Render para a gente ver o que tem lá
print("--- INICIANDO RADIOGRAFIA ---")
print("Diretório atual de trabalho:", os.getcwd())
try:
    print("Arquivos na pasta raiz:", os.listdir())
    if 'templates' in os.listdir():
        print("Arquivos DENTRO de templates:", os.listdir('templates'))
    else:
        print("ALERTA: A pasta 'templates' NÃO foi encontrada na raiz!")
print("--- FIM DA RADIOGRAFIA ---")
# ----------------------------------------

# Dados da Psicóloga (Seu dicionário continua aqui...)
dados_psicologa = {
    'nome': 'Dra. Alessandra Moreira',
        "crp": "06/12345"
    }
    return render_template('index.html', dados=dados_psicologa)

# Rota Sobre Mim
@app.route('/')
def home():
    return render_template('index.html', dados=dados_psicologa)

if __name__ == '__main__':
    app.run(debug=True)
