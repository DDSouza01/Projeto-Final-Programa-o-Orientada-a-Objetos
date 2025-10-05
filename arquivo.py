from produto import Produto 

NOME_ARQUIVO = "produtos.txt" 

def salvar_produtos(lista_produtos: list[Produto]):
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for produto in lista_produtos:
            linha = f"{produto.nome};{produto.preco};{produto.quantidade}\n"
            arquivo.write(linha)

def carregar_produtos():
    list[Produto]


    produtos = []
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            
            nome = dados[0]
            preco = float(dados[1])
            quantidade = int(dados[2])
            
            produto = Produto(nome, preco, quantidade)
            produtos.append(produto)
            
    return produtos

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
        print(f"Produto '{produto.nome}' cadastrado e salvo.")
        self._salvar_automaticamente() 

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio. Cadastre o primeiro produto!")
            return

        print("\n--- LISTAGEM DE PRODUTOS ---")
        for i, produto in enumerate(self.produtos):
            print(f"[{i+1}] {produto}")

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