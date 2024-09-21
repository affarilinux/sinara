from NEO4J.base import Neo4jClient
from NEO4J.tabela import NeoTabela


class DBTecido(Neo4jClient):

    # tem erro em que nao pode ser resolvido em caso de nao tiver a "chave:item"
    # erro "Received notification from DBMS server:""
    def verificar_teclas(self, carac, frequencia):

        tabela = NeoTabela()
        tb = tabela.rotulo_estado("Tecla")

        self.ativar_Neo()

        query = f"CREATE (n:Tecla {{caractere: '{carac}', frequencia: {
            frequencia}}}) RETURN n"

        result = self.executar_query(query)

        self.sair_Neo()
