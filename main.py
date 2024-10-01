from threading import Thread

import arq_trio
import API
import sensitive_ext

from SQLITE.tabela import SqliteTabela
from NEO4J.base import Neo4jClient


class Sistema:

    while_treads = True


if __name__ == '__main__':

    sql_tab = SqliteTabela()

    neo4j = Neo4jClient()
    neo4j.verificar_conexao()

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
