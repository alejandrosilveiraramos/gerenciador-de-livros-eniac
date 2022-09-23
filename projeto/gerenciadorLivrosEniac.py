#Dev (Teste de codigos antes da homolog) Testar conjunto de codigos

#menu // Felipe

#1 cadastro livro // Alejandro

#2 listar os livros cadastrados // David

#3 excluir o livro cadastrado // Marcio e Adriano

#4 finalizar o programa // MC vargas
from time import sleep

decoracao = '-=' * 5 

opcaoMenu = 0

while opcaoMenu != 4:
        print(decoracao, 'Cadastro de Livros', decoracao)
        opcaoMenu = int(input('''\nEscolha uma das opções abaixo:
1 -> Cadastrar Livro
2 -> Listar Livros
3 -> Excluir Livros
4 -> Encerrar o programa
Qual opção: '''))  
        if opcaoMenu == 1:
            livro = str(input('Livro:'))
            while True:
                resp = str(input('Deseja continuar? [S/N]'))
                if resp not in 'SN':
                    print('Opção inválida, Digite S ou N')
                if resp in 'N':
                    break    
        elif opcaoMenu == 2:
            print('2')
        elif opcaoMenu == 3:
            print('3')
        elif opcaoMenu == 4:
            print('Programa Finalizado.')
        else:
            print('Opcão inválida\n')
            sleep(1) 





        
                 
              
    