from neo4j import GraphDatabase

from NEO4J.neo import Neo


class Neo4jClient:

    def ativar_Neo(self):

        # Criando o driver
        self.driver = GraphDatabase.driver(
            Neo.url, auth=(Neo.username, Neo.password))
        print("ativar")

    def executar_query(self, query):

        try:
            with self.driver.session() as session:
                result = session.run(query)

                # Verificando se há resultados
                records = result.data()
                if records:
                    return records
                else:

                    return "s/dados"

        except Exception as e:
            print(f'Erro capturado {e.__class__}: {e}')
            return "erro query"

    def commit_Neo(self):

        with self.driver.session() as session:
            # Iniciando a transação
            with session.begin_transaction() as tx:
                # Executando a consulta dentro da transação
                query = "CREATE (n:Pessoa {nome: 'João', idade: 30}) RETURN n"
                result = tx.run(query)
                # Fazendo o commit manualmente
                tx.commit()
                print("Nó criado com sucesso e transação comitada.")

    def sair_Neo(self):

        print("sair")
        self.driver.close()
