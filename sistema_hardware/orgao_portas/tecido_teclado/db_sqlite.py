from SQLITE.base import BaseSqlite


class SqliteTecido(BaseSqlite):

    def verificar_caractere(self, caractere: str) -> bool:

        self.ativar_with()

        tabela = "SELECT COUNT(*) FROM tb_CARACTERE WHERE caractere = ?"
        self.withdb.execute(tabela, (caractere,))
        resultado = self.withdb.fetchone()

        return resultado[0] > 0

    def obter_lista_frequencias(self) -> list:

        self.ativar_with()

        tabela = "SELECT frequencia FROM tb_CARACTERE"

        self.withdb.execute(tabela)

        resultados = self.withdb.fetchall()  # Isso retorna uma lista de tuplas
        # Extrai o valor de cada tupla
        lista_frequencias = [resultado[0] for resultado in resultados]

        return lista_frequencias

    def inserir_caractere(self, caractere: str, frequencia: int) -> None:

        self.ativar_banco()

        tabela = "INSERT INTO tb_CARACTERE (caractere, frequencia) VALUES (?, ?)"

        self.cursorsq.execute(tabela, (caractere, frequencia))

        self.commit_banco()
        self.sair_banco()

    def verificar_frequencia_por_caractere(self, caractere: str) -> int:

        tabela = "SELECT frequencia FROM tb_CARACTERE WHERE caractere = ?"

        self.withdb.execute(tabela, (caractere,))
        resultado = self.withdb.fetchone()  # Retorna uma única linha

        return resultado[0]  # Retorna a frequência encontrada
