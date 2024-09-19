# api2.py
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json  # Recebe os dados da requisição
    print(f"API 2: Dados recebidos: {data}")
    return jsonify({"status": "Dados recebidos com sucesso pela API 2!"}), 200

# api1 - teclado


def send_teclado():
    # Função para capturar entrada do usuário
    while True:
        data_input = input("API 2: Digite algo para enviar à API 1: ")
        data = {"mensagem": data_input}

        # Envia uma requisição HTTP POST para a API 1
        response = requests.post(
            'http://localhost:5010/api/teclado', json=data)
        print(f"API 2: Resposta da API 1: {response.json()}")


if __name__ == '__main__':
    # Inicia o Flask em uma thread separada
    from threading import Thread
    Thread(target=lambda: app.run(
        port=5001, debug=True, use_reloader=False)).start()

    # Função para capturar e enviar dados manualmente
    send_teclado()
