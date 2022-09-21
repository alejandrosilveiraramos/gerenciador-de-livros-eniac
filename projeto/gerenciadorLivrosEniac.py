#Dev (Teste de codigos antes da homolog) Testar conjunto de codigos

#menu // Felipe

#1 cadastro livro // Alejandro

#2 listar os livros cadastrados // David

#3 excluir o livro cadastrado // Marcio e Adriano

#4 finalizar o programa // MC vargas
from time import sleep

decoracao = '-=' * 5 

livraria = []
livro = {}

opcaoMenu = 0

while opcaoMenu != 4:
    try:
        print(decoracao, 'Cadastro de Livros', decoracao)
        opcaoMenu = int(input('''\nEscolha uma das opções abaixo:
1 -> Cadastrar Livro
2 -> Listar Livros
3 -> Excluir Livros
4 -> Encerrar o programa
Qual opção: '''))  
        while True:
            if opcaoMenu == 1:  
                livro['Nome'] =  str(input('Nome do Livro: '))
                livro['Editora'] =  str(input('Editora: '))
                livro['Autor'] =  str(input('Autor: '))
                livro['Genero'] =  str(input('Genêro: '))
                livro['Ano Publicação'] =  int(input('Ano de Publicação: '))
                livro['ISBN'] =  int(input('ISBN: '))

                livraria.append(livro.copy())
                while True:
                    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
                    if resp in 'SN':
                        break
                    print('ERRO! Responda apensa S ou N')
                if resp in 'N':
                    break 
            else:
                print('Opção inválida')
                sleep(1)
                break          
    except:
        print('Opcão inválida\n')
        sleep(1) 




        
                 
              
    