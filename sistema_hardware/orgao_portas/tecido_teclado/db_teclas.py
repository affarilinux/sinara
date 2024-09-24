from NEO4J.base import Neo4jClient
from NEO4J.tabela import NeoTabela


class DBTecido(Neo4jClient):

    # tem erro em que nao pode ser resolvido em caso de nao tiver a "chave:item"
    # erro "Received notification from DBMS server:""
    def verificar_rotulo_caractere(self):

        tabela = NeoTabela()
        tb = tabela.rotulo_estado("CARACTERE")

        # rotulo nao existe
        if tb == "KeyError":

            return "KeyError"

        else:

            return "rotulo"

    def inserir_string(self, carac, frequencia):

        self.ativar_Neo()

        query = f"CREATE (n:CARACTERE {{caractere: '{carac}', frequencia: {
            frequencia}}}) RETURN n"

        result = self.executar_query(query)

        self.sair_Neo()

    def verificar_caractere(self, caractere):

        self.ativar_Neo()

        query = "MATCH (t:CARACTERE {caractere: $caractere}) RETURN t"
        results = self.executar_query_2(
            query, parametros={"caractere": caractere})

        self.sair_Neo()

        # Verifica se há algum resultado
        if results and len(results) > 0:
            return True  # Caractere existe
        else:
            return False  # Caractere não existe

    def executar_query_2(self, query, parametros=None):

        with self.driver.session() as session:
            if parametros:
                result = session.run(query, parametros)
            else:
                result = session.run(query)

            # Convertendo o resultado em uma lista de registros
            return [record for record in result]

    def lista_frequencias(self):

        # A query Cypher para listar apenas as frequências
        query = """
        MATCH (t:Tecla)
        RETURN t.frequencia AS frequencia
        ORDER BY t.frequencia DESC
        """

        # Executa a query e retorna os resultados
        results = self.executar_query(query)

        # Converte os resultados em uma lista de frequências
        lista_frequencias = [r['frequencia'] for r in results]
        return lista_frequencias
