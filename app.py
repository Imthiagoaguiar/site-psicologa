import os
from flask import Flask, render_template

app = Flask(__name__)

# --- BLOCO DE RADIOGRAFIA (DEBUG) ---
print("--- INICIANDO RADIOGRAFIA ---")
try:
    print("Diretório atual:", os.getcwd())
    arquivos = os.listdir()
    print("Arquivos na raiz:", arquivos)
    
    if 'templates' in arquivos:
        print("Arquivos DENTRO de templates:", os.listdir('templates'))
    else:
        print("ALERTA: A pasta 'templates' NÃO existe aqui!")
except Exception as e:
    print(f"ERRO NA RADIOGRAFIA: {e}")
print("--- FIM DA RADIOGRAFIA ---")
# ------------------------------------

# Seus dados originais
dados_psicologa = {
    'nome': 'Dra. Alessandra Moreira',
    'crp': '08/12345',
    'telefone': '5541999999999',
    'instagram': '@dra.alessandra',
    'especialidades': [
        'Ansiedade e Pânico',
        'Terapia de Casal',
        'Depressão',
        'Autoestima'
    ],
    'sobre_mim': """
    Sou psicóloga clínica com abordagem em Terapia Cognitivo-Comportamental.
    Meu objetivo é ajudar você a encontrar equilíbrio emocional e autoconhecimento
    em um ambiente acolhedor e seguro.
    """
}

@app.route('/')
def home():
    # O Flask procura automaticamente dentro da pasta 'templates'
    return render_template('index.html', dados=dados_psicologa)

if __name__ == '__main__':
    app.run(debug=True)
