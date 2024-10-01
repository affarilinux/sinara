from SQLITE.base import BaseSqlite


class SqliteTabela(BaseSqlite):

    def __init__(self) -> None:

        # banco de dados
        self.ativar_with()

        """   teclado       """

        self.withdb.execute(
            """CREATE TABLE if not exists tb_CARACTERE(

            ID_tecla INTEGER PRIMARY KEY AUTOINCREMENT,

            caractere  TEXT,   -- variavel string
            frequencia INT     -- variavel fixo 1 ate 10 000 iguais-nao
            
            )""")
