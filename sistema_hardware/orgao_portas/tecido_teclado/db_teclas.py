from NEO4J.base import Neo4jClient
from NEO4J.tabela import NeoTabela


class DBTecido(Neo4jClient):

    # tem erro em que nao pode ser resolvido em caso de nao tiver a "chave:item"
    # erro "Received notification from DBMS server:""
    def verificar_teclas(self, carac):

        self.ativar_Neo()

        tabela = NeoTabela()
        tabela.rotulo_estado("Tecla")

        print(tabela)

        self.sair_Neo()
        """try:
            query = f"MATCH (n:Tecla {{caractere: '{carac}'}}) RETURN n"
            results = self.executar_query(query)
        except Exception as err:
            print(f"Ocorreu um erro: {err}")
            results = None

        self.sair_Neo()

        if results and results != "erro":
            print(f"Tecla '{carac}' encontrada.")
            return True
        else:
            print(f"Tecla '{carac}' não encontrada ou erro na consulta.")
            return False"""
