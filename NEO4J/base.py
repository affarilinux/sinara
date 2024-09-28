from neo4j import GraphDatabase

from NEO4J.neo import Neo


class Neo4jClient:

    def ativar_Neo(self):

        # Criando o driver
        self.driver = GraphDatabase.driver(
            Neo.url, auth=(Neo.username, Neo.password))
        # print("ativar")

    def commit_Neo(self):

        with self.driver.session() as session:
            # Iniciando a transação
            with session.begin_transaction() as tx:
                # Executando a consulta dentro da transação
                query = "CREATE (n:Pessoa {nome: 'João', idade: 30}) RETURN n"
                result = tx.run(query)
                # Fazendo o commit manualmente
                tx.commit()
                # print("Nó criado com sucesso e transação comitada.")

    def sair_Neo(self):

        # print("sair")
        self.driver.close()
