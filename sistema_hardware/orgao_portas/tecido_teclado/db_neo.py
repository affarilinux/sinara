from NEO4J.base import Neo4jClient


class NeoTecidoSS(Neo4jClient):

    def inserir_celular_Sensor(self, id, SS):

        valor = 0.000000001

        self.ativar_Neo()

        query = f"""CREATE (n:SENSOR_TECLA {{ID: '{id}', sensor: '{
            SS}', vida:{valor}}}) RETURN n"""

        with self.driver.session() as session:
            result = session.run(query)

        self.sair_Neo()

    # futuramente a função ID vai sumir do banco.
    def get_max_ID(self):

        self.ativar_Neo()

        query = f"""MATCH (t:SENSOR_TECLA) RETURN max(t.ID) AS MaxID"""

        with self.driver.session() as session:
            result = session.run(query)
            max_ID = result.single()[0]  # Obtém o valor máximo
            return max_ID

        self.sair_Neo()

        # Verifica se há algum resultado
        if carac_ver and len(carac_ver) > 0:

            return True  # Caractere existe
        else:

            return False  # Caractere não existe

    def lista_celular_sensor(self):

        self.ativar_Neo()

        query = """MATCH (s:SENSOR_TECLA) RETURN s.ID AS ID, s.sensor AS sensor"""

        with self.driver.session() as session:
            result = session.run(query)

            # Converte os resultados em uma lista de frequências
            lista_celular_sensor = [record.data() for record in result]

        self.sair_Neo()

        return lista_celular_sensor


class Valor:

    def inserir_string(self, carac, frequencia):

        self.ativar_Neo()

        query = f"""CREATE (n:CARACTERE {{caractere: '{carac}', frequencia: {
            frequencia}}}) RETURN n"""

        with self.driver.session() as session:
            result = session.run(query)

        self.sair_Neo()

    def verificar_caractere(self, caractere):

        self.ativar_Neo()

        query = """MATCH (t:CARACTERE {caractere: $caractere}) RETURN t"""

        with self.driver.session() as session:
            # nao pode ficar dentro run ={}
            parametros = {"caractere": caractere}
            result = session.run(query, parametros)

            carac_ver = [record for record in result]

        self.sair_Neo()

    def lista_frequencias(self):

        self.ativar_Neo()

        # A query Cypher para listar apenas as frequências
        query = """
        MATCH (t:CARACTERE)
        RETURN t.frequencia AS frequencia
        ORDER BY t.frequencia DESC
        """

        # Executa a query e retorna os resultados
        with self.driver.session() as session:
            results = session.run(query)

            # Converte os resultados em uma lista de frequências
            lista_frequencias = [r['frequencia'] for r in results]

        self.sair_Neo()

        return lista_frequencias

    def encontrar_frequencia_caractere(self, caractere):

        self.ativar_Neo()

        # Consulta Cypher para encontrar a frequência de um caractere específico
        query = """
        MATCH (c:CARACTERE {caractere: $caractere})
        RETURN c.frequencia AS frequencia
        """

        with self.driver.session() as session:
            # nao pode ficar dentro run ={}
            parametros = {"caractere": caractere}
            resultado = session.run(query, parametros)

            # Retorna todos os resultados em uma lista de dicionários
            result_freq = [record.data() for record in resultado]

        frequencia = result_freq[0].get('frequencia')

        self.sair_Neo()

        return frequencia
