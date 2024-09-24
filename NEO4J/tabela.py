from NEO4J.base import Neo4jClient


class NeoTabela(Neo4jClient):

    # nao tem como criar rotulo sem adicionar os objetos
    def rotulo_estado(self, rotulo):

        try:
            # Ativa o banco de dados antes de prosseguir
            self.ativar_Neo()

            # Verifica se o rótulo existe
            rot = self.verificar_rotulo(rotulo)

            if not rot:

                return "KeyError"  # Indica que o rótulo não existe

            else:
                return "Rótulo existe"  # Rótulo foi encontrado

        except AttributeError as e:
            return f"Erro de ativação: {e}"

        finally:
            self.sair_Neo()  # Sempre fecha a conexão, mesmo se houver erro

    # Método para verificar se um rótulo existe no banco de dados
    def verificar_rotulo(self, rotulo):
        query = "CALL db.labels()"  # Chama a função para listar os rótulos no Neo4j

        try:
            # Executa a query para buscar todos os rótulos
            results = self.executar_query(query)
            # Extrai os rótulos existentes da resposta da consulta
            rotulos_existentes = [r[0] for r in results]

            # Verifica se o rótulo passado está na lista de rótulos
            return rotulo in rotulos_existentes

        except Exception as e:
            return f"Erro ao verificar rótulo: {e.__class__.__name__} - {e}"

        """# tem que ter ativar banco aqui se  nao dar erro
        #  <class 'AttributeError'>:
        self.ativar_Neo()

        rot = self.verificar_rotulo(rotulo)

        if rot == "KeyError":

            self.sair_Neo()
            return "KeyError"

        else:
            return "dif/keyerror"

    # tipo tabela

    def verificar_rotulo(self, rotulo):

        query = "CALL db.labels()"

        try:
            results = self.executar_query(query)
            # Extrai os rótulos da resposta
            rotulos_existentes = [r[0] for r in results]
            return rotulo in rotulos_existentes

        except KeyError:

            return "KeyError"

        except Exception as e:

            return f"verificar rotulo {e.__class__}"""
