def menu():

    decoracao = '-=' * 5 
    
    while True:
                
        opcaoMenu = str(input('''\n\n\n{}\033[93mGERENCIADOR DE LIVROS GUIDOLOOPING\033[m{}\n\033[96mMenu\033[m\n
Escolha uma das opções abaixo:
1 {}-> Cadastrar Livro{}
2 {}-> Listar Livros{}
3 {}-> Excluir Livros{}
4 {}-> Encerrar o programa{}\n
{}Qual opção:{} '''.format(decoracao, decoracao,'\033[96m', '\033[m', '\033[96m', '\033[m', '\033[96m', '\033[m', '\033[96m', '\033[m', '\033[96m', '\033[m')))  

        if opcaoMenu == '1':
            print('1')
        elif opcaoMenu == '2':
            print('2')
        elif opcaoMenu == '3':
            print('3')
        elif opcaoMenu == '4':
            print('4 out')
            break


