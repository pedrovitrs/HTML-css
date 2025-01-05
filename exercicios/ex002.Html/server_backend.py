from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Caminho para salvar os dados
DATA_FOLDER = 'dados'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

@app.route('/salvar', methods=['POST'])
def salvar():
    try:
        # Obter os dados do cliente
        dados = request.get_json()

        # Validar os dados recebidos
        if not all(key in dados for key in ['name', 'address', 'city', 'postalCode']):
            return jsonify({"error": "Campos obrigatórios faltando"}), 400

        # Nome do arquivo para salvar os dados
        arquivo = os.path.join(DATA_FOLDER, f"{dados['name'].replace(' ', '_')}.json")

        # Salvar os dados em um arquivo JSON
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        return jsonify({"message": "Dados salvos com sucesso!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
