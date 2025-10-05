Projeto Final de POO – Sistema de Gestão de Estoque
Descrição Geral

Este projeto tem como objetivo implementar um Sistema de Gestão de Estoque em Python, aplicando de forma prática os principais conceitos de Programação Orientada a Objetos (POO).

O sistema permite cadastrar, listar, remover e atualizar produtos em estoque, controlando suas quantidades e preços, com persistência automática de dados em arquivo.

Objetivos de Aprendizagem

Durante o desenvolvimento do projeto, o aluno deve aplicar os seguintes conceitos fundamentais de POO:

Classes e objetos

Construtores e autorreferência (self)

Encapsulamento com @property e @setter (atributos privados __atributo)

Tratamento de exceções com try/except

Persistência de dados utilizando with open ... as arquivo

Estrutura Obrigatória
1. Classe Produto

Função: Representa um produto individual no estoque.

Atributos privados:

__nome: str

__preco: float

__quantidade: int

Encapsulamento:

Métodos @property e @setter para controle e validação dos atributos.

Exemplo: não permitir valores negativos para preço ou quantidade.

Métodos obrigatórios:

__init__(self, nome, preco, quantidade) → inicializa os atributos.

__str__(self) → retorna uma string formatada com as informações do produto.

adicionar_estoque(self, quantidade) → incrementa a quantidade.

remover_estoque(self, quantidade) → decrementa a quantidade com validação.

2. Classe Estoque

Função: Gerencia a lista de produtos e suas operações.

Atributo:

produtos (lista de objetos Produto)

Métodos obrigatórios:

adicionar_produto(self, produto) → adiciona novo produto e salva no arquivo.

listar_produtos(self) → exibe todos os produtos cadastrados.

remover_produto(self, nome_produto) → remove produto pelo nome e atualiza o arquivo.

adicionar_quantidade(self, nome_produto, quantidade) → aumenta o estoque de um produto.

remover_quantidade(self, nome_produto, quantidade) → reduz o estoque de um produto.

carregar_produtos(self) → lê os dados do arquivo produtos.txt ao iniciar o sistema.

3. Persistência de Dados

Arquivo: produtos.txt
Cada linha representa um produto no formato:

nome;preco;quantidade


Regras:

Todas as modificações (adição, remoção, alteração de quantidade) são salvas automaticamente.

Para atualizar ou remover produtos, o arquivo é reescrito completamente.

O carregamento dos produtos é feito na inicialização do sistema.

4. Estrutura Modular do Projeto

O projeto deve ser organizado em módulos para facilitar a manutenção e a clareza do código:

Arquivo	Descrição
produto.py	Contém a classe Produto, com atributos privados, propriedades, setters e métodos de controle de estoque.
estoque.py	Contém a classe Estoque, responsável pela gestão da lista de produtos e integração com o arquivo de persistência.
arquivo.py	Funções auxiliares para salvar e carregar dados do arquivo produtos.txt.
menu.py	Implementa o menu interativo, incluindo o tratamento de exceções e as opções do sistema.
main.py	Arquivo principal que inicializa o estoque, chama o menu e integra todos os módulos.
5. Menu do Sistema
===== Sistema de Gestão de Estoque =====
1. Cadastrar novo produto
2. Listar produtos
3. Adicionar quantidade a um produto
4. Remover quantidade de um produto
5. Remover produto
0. Sair


Regras do menu:

O menu deve permanecer em loop até que o usuário escolha 0 – Sair.

Todas as alterações devem ser salvas automaticamente.

O sistema deve tratar exceções para entradas inválidas, como:

Preço ou quantidade negativa

Nome inexistente no estoque

Erros de conversão de tipos (ex.: ValueError)

Boas Práticas de Implementação

Utilizar comentários explicativos no código.

Seguir o padrão PEP 8 de formatação de código Python.

Manter o código limpo, modular e fácil de compreender.

Não utilizar bibliotecas externas — apenas a biblioteca padrão do Python.

Tecnologias Utilizadas

Linguagem: Python 3.x

Bibliotecas: Apenas biblioteca padrão (os, sys, etc.)

Execução do Projeto

Clone ou copie os arquivos para uma pasta local.

Certifique-se de que todos os módulos (produto.py, estoque.py, arquivo.py, menu.py, main.py) estejam no mesmo diretório.

Execute o projeto com o comando:

python main.py


Interaja com o menu para cadastrar e gerenciar produtos no estoque.

Exemplo de Execução
===== Sistema de Gestão de Estoque =====
1. Cadastrar novo produto
2. Listar produtos
3. Adicionar quantidade a um produto
4. Remover quantidade de um produto
5. Remover produto
0. Sair
Escolha uma opção: 1
Digite o nome do produto: Caneta
Digite o preço: 2.50
Digite a quantidade: 100
Produto 'Caneta' cadastrado com sucesso!

Autor

Projeto desenvolvido por: Danilo e Luan
Disciplina: Programação Orientada a Objetos
Instituição: Instituto Federal Ceará - Campus Maranguape
Ano: 2025
