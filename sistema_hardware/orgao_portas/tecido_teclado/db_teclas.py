from NEO4J.base import Neo4jClient


class DBTecido(Neo4jClient):

    def verificar_teclas(self, carac):

        self.ativar_Neo()

        print(carac)
        self.sair_Neo()

        return
