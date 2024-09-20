import requests
from flask import Flask, request, jsonify
from threading import Thread

class FlaskAPI:
    def __init__(self, shared_tecla):

        self.app = Flask(__name__)
        # Variável compartilhada sensitive
        self.shared_tecla = shared_tecla
        self.setup_routes()

    # 1 treads - teclado - api1
    def setup_routes(self):

        @self.app.route('/api/teclado', methods=['POST'])
        def receive_data():
            # Recebe os dados da requisição-{'mensagem':xx}
            teclado = request.json
            print(f"API 1: Dados recebidos: {teclado}")

            # inserir na lista classe sensor
            self.shared_tecla.append(teclado['mensagem'])

            return jsonify({"status": "Dados recebidos com sucesso pela API 1!"}), 200

    def run(self):

        # Inicia o servidor Flask em uma thread separada
        flask_thread = Thread(target=lambda: self.app.run(
            port=5010, debug=True, use_reloader=False))
        flask_thread.start()

    # 2 treads executada -  tela
    def send_data(self):

        # Função para capturar entrada do usuário
        while True:
            data_input = input("API 1: Digite algo para enviar à API 2: ")
            data = {"mensagem": data_input}

            try:
                # Envia uma requisição HTTP POST para a API 2
                response = requests.post(
                    'http://localhost:5001/api/data', json=data)
                print(f"API 1: Resposta da API 2: {response.json()}")

            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar dados para a API 2: {e}")

    def start_send_data_thread(self):

        # Inicia a função send_data em uma thread separada
        send_data_thread = Thread(target=self.send_data)
        send_data_thread.start()
