from NEO4J.base import Neo4jClient


class NeoTabela(Neo4jClient):

    # nao tem como criar rotulo sem adicionar os objetos
    def rotulo_estado(self, rotulo):

        # tem que ter ativar banco aqui se  nao dar erro
        #  <class 'AttributeError'>:
        self.ativar_Neo()

        rot = self.verificar_rotulo(rotulo)

        self.sair_Neo()

        if rot == "KeyError":

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

            return f"verificar rotulo {e.__class__}"
