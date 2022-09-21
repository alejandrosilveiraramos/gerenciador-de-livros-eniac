#Dev (Teste de codigos antes da homolog) Testar conjunto de codigos

#menu // Felipe

#1 cadastro livro // Alejandro

#2 listar os livros cadastrados // David

#3 excluir o livro cadastrado // Marcio e Adriano

#4 finalizar o programa // MC vargas
from time import sleep

decoracao = '-=' * 5 

while True:
        try:
            print(decoracao, 'Cadastro de Livros', decoracao)
            opcaoMenu = str(input('''\nEscolha uma das opções abaixo:
1 -> Cadastrar Livro
2 -> Listar Livros
3 -> Excluir Livros
4 -> Encerrar o programa
Qual opção: '''))
        except ValueError:
            print('Opcão inválida\n')
            sleep(1)
        
                 
              
    