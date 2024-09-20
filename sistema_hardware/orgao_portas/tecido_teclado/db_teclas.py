from NEO4J.base import Neo4jClient


class DBTecido(Neo4jClient):

    def verificar_teclas(self, carac):

        self.ativar_Neo()

        query = f"MATCH (n:Tecla {{caractere: '{carac}'}}) RETURN n"
        results = self.executar_query(query)

        self.sair_Neo()

        if results:
            return True
        else:
            return False
