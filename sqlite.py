import sqlite3

class Sqlite:
    def __init__(self,database,nome_table) -> None:
        self._database = database
        self._nome_table = nome_table

    def criar_banco(self) ->None:
        """Criar um Data base e uma tabela caso a tabela 
        não exista
        """
        banco = sqlite3.connect(self._database)
        cursor = banco.cursor()
        script = (f"CREATE TABLE IF NOT EXISTS "+ 
        f"{self._nome_table} (nome text,vendedor text,avaliacao "+
        "integer,valor text,parcelas text)")
        
        try:
            cursor.executescript(script)
            banco.commit()
            banco.close()
        except:
            print('Banco ja existe!')
        


    def inserir_info(self,
                    nome:str,
                    vendedor:str,
                    avaliacao:int,
                    valor:str,
                    parcelas:str
                    )->None:
        """Insere novas linhas na tabela 

        Args:
            nome (str): nome produto
            vendedor (str): vendedor do produto
            avaliacao (int): avaliação do produto
            valor (str): valor do produto
            parcelas (str): parcelas do produto
        """
        banco = sqlite3.connect(self._database)
        cursor = banco.cursor()
        script = (f'INSERT INTO {self._nome_table} (nome,vendedor,avaliacao,'+
                'valor,parcelas) VALUES (?,?,?,?,?)')
        cursor.execute(script,(nome,vendedor,avaliacao,valor,parcelas))
        banco.commit()
        banco.close()


    def dropar_tabela(self):
        """Excluir a tabela do banco informado

        Args:
            database (str): banco de dados
            nome_table (str): tabela a ser excluida
        """
        
        banco = sqlite3.connect(self._database)
        cursor = banco.cursor()
        script = (f'DROP TABLE IF EXISTS {self._nome_table}')
        cursor.executescript(script)
        banco.commit()
        banco.close()