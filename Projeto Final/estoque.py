from produto import Produto
from arquivo import carregar_produtos, salvar_produtos

class Estoque:
    
    def __init__(self):
        self.produtos: list[Produto] = carregar_produtos()
        print("Estoque inicializado com sucesso.")

    def _salvar_automaticamente(self):
        salvar_produtos(self.produtos)

    def _buscar_produto(self, nome_produto: str):
        nome_formatado = nome_produto.strip().lower()
        for produto in self.produtos:
            if produto.nome.lower() == nome_formatado:
                return produto
        return None 

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' cadastrado e salvar.")
        self._salvar_automaticamente() 

    def remover_produto(self, nome_produto: str):
        produto_a_remover = self._buscar_produto(nome_produto)
        self.produtos.remove(produto_a_remover)
        print(f"Produto '{produto_a_remover.nome}' removido do estoque.")
        self._salvar_automaticamente() 

    def adicionar_quantidade(self, nome_produto: str, quantidade: int):
        produto = self._buscar_produto(nome_produto)
        produto.adicionar_estoque(quantidade) 
        self._salvar_automaticamente() 

    def remover_quantidade(self, nome_produto: str, quantidade: int):
        produto = self._buscar_produto(nome_produto)
        produto.remover_estoque(quantidade) 
        self._salvar_automaticamente() 