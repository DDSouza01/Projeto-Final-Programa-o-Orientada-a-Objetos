class Produto:

   # Representa um produto individual no estoque.
    
    
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome 
        self.preco = preco 
        self.quantidade = quantidade  
        
    # nome (privado)
    @property
    def nome(self):
    
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome.strip()
        
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        self.__preco = novo_preco
        
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade: int):
        self.__quantidade = nova_quantidade
    
    def adicionar_estoque(self, qtd_entrada: int):
        self.quantidade += qtd_entrada 
        print(f"{qtd_entrada} unidades de '{self.nome}' adicionadas ao estoque.")

    def remover_estoque(self, qtd_saida: int):
        self.quantidade -= qtd_saida
        print(f"{qtd_saida} unidades de '{self.nome}' removidas do estoque.")

    def __str__(self):
        return (f"Nome: {self.nome} ,  Preço: R$ {self.preco:.2f} , Estoque: {self.quantidade} unidades")