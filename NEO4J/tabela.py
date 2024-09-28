from NEO4J.base import Neo4jClient


class NeoTabela(Neo4jClient):

    # nao tem como criar rotulo sem adicionar os objetos
    def verificar_rotulo_CARACTERE(self, rotulo):

        self.ativar_Neo()

        query = """CALL db.labels()"""  # Chama a função para listar os rótulos no Neo4j

        # Executa a query para buscar todos os rótulos
        with self.driver.session() as session:
            results = session.run(query)
            # Extrai os rótulos existentes da resposta da consulta
            rotulos_existentes = [r[0] for r in results]

        # Verifica se o rótulo passado está na lista de rótulos
        print("01")
        rot = rotulo in rotulos_existentes

        self.sair_Neo()  # Sempre fecha a conexão, mesmo se houver erro

        if not rot:

            return "KeyError"  # Indica que o rótulo não existe

        else:

            return "ROTULO EXISTE"
