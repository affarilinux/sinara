from threading import Thread

import arq_trio
import API
import sensitive_ext

from NEO4J.tabela import NeoTabela


class Sistema:

    while_treads = True


if __name__ == '__main__':

    # Instancia e executa a classe FlaskAPI
    flask_api = API.FlaskAPI(
        sensitive_ext.SensorExt.shared_teclado
    )
    flask_api.run()
    flask_api.start_send_data_thread()

    # Instancia e executa a classe TrioTasks
    trio_tasks = arq_trio.TrioTasks()
    # Inicia o loop Trio em uma thread separada
    trio_thread = Thread(target=trio_tasks.start_trio)
    trio_thread.start()
