#nome,valor,vendedor,parcelas e valor, avaliação,cupons de desconto 

class Mercadoria:
    def __init__(self,
                 nome,
                 vendedor,
                 avaliacao,
                 valor,
                 parcelas,
                 ) -> None:
        self._nome = nome
        self._valor = valor 
        self._vendedor = vendedor
        self._avaliacao = avaliacao
        self._parcelas= parcelas

    def retorna_nome(self)->str:
        return self._nome

    def retorna_vendedor(self)->str:
        return self._vendedor
    
    def retorna_avaliacao(self)->float:
        return self._avaliacao

    def retorna_parcelas(self)-> str:
        return self._parcelas

    def retorna_valor(self)->str:
        return self._valor

    def __str__(self) -> str:
        return f'A mercadoria {self._nome} custa {self._valor} e é vendida por {self._vendedor}'

