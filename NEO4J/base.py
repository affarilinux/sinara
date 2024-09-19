from neo4j import GraphDatabase

from Neo4j.neo import Neo

class Neo4jClient:

    def ativar_banco(self):

        # Criando o driver
        self.driver = GraphDatabase.driver(Neo.url, auth=(Neo.username, Neo.password))
        print(12)
    def commit_banco(self):

        with self.driver.session() as session:
        # Iniciando a transação
            with session.begin_transaction() as tx:
                # Executando a consulta dentro da transação
                query = "CREATE (n:Pessoa {nome: 'João', idade: 30}) RETURN n"
                result = tx.run(query)
                # Fazendo o commit manualmente
                tx.commit()
                print("Nó criado com sucesso e transação comitada.")

    def sair_banco(self):
        print(13)
        self.driver.close()