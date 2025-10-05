from estoque import Estoque
from produto import Produto

estoque = Estoque()

def exibir_menu():
    print("===== Sistema de Gestão de Estoque =====")
    print("1. Cadastrar novo produto")
    print("2. Listar produtos")
    print("3. Adicionar quantidade a um produto (Entrada)")
    print("4. Remover quantidade de um produto (Saída)")
    print("5. Remover produto")
    print("0. Sair")
   

def obter_entrada(mensagem, tipo=str):
    return tipo(input(mensagem).strip())

def cadastrar_produto():

    print("\n--- CADASTRO DE PRODUTO ---")
    
    nome = obter_entrada("Nome do produto: ")
    preco = obter_entrada("Preço (ex: 10.50): ", float)
    quantidade = obter_entrada("Quantidade inicial: ", int)
    novo_produto = Produto(nome, preco, quantidade)
    estoque.adicionar_produto(novo_produto)
        
def listar_produtos():
    estoque.listar_produtos()

def alterar_quantidade(tipo_operacao: str):
    print(f"\n--- {tipo_operacao.upper()} DE QUANTIDADE ---")
    
    nome = obter_entrada("Nome do produto: ")
    quantidade = obter_entrada("Quantidade a ser movimentada: ", int)
    
    if tipo_operacao == "Adicionar":
        estoque.adicionar_quantidade(nome, quantidade)
    else:
        estoque.remover_quantidade(nome, quantidade)
            

def remover_produto():
    print("\n--- REMOVER PRODUTO ---")
    
    nome = obter_entrada("Nome do produto a remover: ")
    
    estoque.remover_produto(nome)


def executar_menu():
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ").strip() 
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            alterar_quantidade("Adicionar")
        elif opcao == '4':
            alterar_quantidade("Remover")
        elif opcao == '5':
            remover_produto()
        elif opcao == '0':
            print("\nSistema encerrado. Todos os dados foram salvos.")
            break 
        else:
            print("Opção inválida. Digite um número de 0 a 5.")