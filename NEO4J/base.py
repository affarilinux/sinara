from neo4j import GraphDatabase

from NEO4J.neo import Neo


class Neo4jClient:

    def ativar_Neo(self):

        # Criando o driver
        self.driver = GraphDatabase.driver(
            Neo.url, auth=(Neo.username, Neo.password))

    def commit_Neo(self):

        with self.driver.session() as session:
            # Iniciando a transação
            with session.begin_transaction() as tx:
                # Executando a consulta dentro da transação
                query = "CREATE (n:Pessoa {nome: 'João', idade: 30}) RETURN n"
                result = tx.run(query)
                # Fazendo o commit manualmente
                tx.commit()

    def sair_Neo(self):

        self.driver.close()

    def verificar_conexao(self):
        try:

            self.ativar_Neo()

            with self.driver.session() as session:
                # Executa um comando simples, como 'RETURN 1'
                result = session.run("RETURN 1")
                # Verifica se obteve resposta
                if result.single()[0] == 1:
                    print("Conexão bem-sucedida com o Neo4j!")
                else:
                    print("Conexão falhou.")

            # Fecha o driver
            self.sair_Neo()

        # except Erro ao conectar:
        except Exception as e:

            print("#@"*20)
            print(f"Erro ao conectar: {e}")
            print("#@"*20, "\n")
