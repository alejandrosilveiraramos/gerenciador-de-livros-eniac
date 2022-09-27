
import re
from collections import Counter
from time import sleep

livraria = []

print( '''                                                                
░░              ░░                    ░░                    ░░                    ░░    
                                                                                        
                                                                                        
                              ██████████          ██████████                            
░░      ░░            ░░    ██          ██  ░░  ██          ██    ░░      ░░            
                          ██              ██  ██              ██                        
                        ██      ██  ██      ██      ██  ██      ██                      
                      ████  ██          ██  ██  ██          ██  ████                    
        ░░      ░░  ██░░██                  ██                  ██░░██    ░░      ░░    
                    ██░░██      ██  ██      ██      ██  ██      ██░░██                  
                    ██░░██  ██          ██  ██  ██          ██  ██░░██                  
                    ██░░██                  ██                  ██░░██                  
                    ██░░██                  ██                  ██░░██                  
                    ██░░██  ████████████    ██    ████████████  ██░░██                  
                    ██░░████            ██  ██  ██            ████░░██                  
░░                  ██░░██  ████████████  ██████  ████████████  ██░░██                  
                    ██░░████░░░░░░░░░░░░██  ██  ██░░░░░░░░░░░░████░░██                  
                    ██░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░██                  
                    ██░░░░░░░░██████████░░░░░░░░░░██████████░░░░░░░░██                  
                    ██░░░░████          ██████████          ████░░░░██                  
                      ████                                      ████                    
                                                                                        
                                                                                        
░░                                                                           
      ''')


livraria = []
livro = {}

opcaoMenu = 0

decoracao = '-=' * 5 
print(decoracao, '\033[93mGERENCIADOR DE LIVROS GUIDOLOOPING\033[m', decoracao)
while opcaoMenu != '4':
        
        sleep(.8)
        
        opcaoMenu = str(input('''\n\n\n\033[96mMenu\033[m\n
Escolha uma das opções abaixo:
1 {}-> Cadastrar Livro{}
2 {}-> Listar Livros{}
3 {}-> Excluir Livros{}
4 {}-> Encerrar o programa{}\n
{}Qual opção:{} '''.format('\033[96m', '\033[m', '\033[96m', '\033[m', '\033[96m', '\033[m', '\033[96m', '\033[m', '\033[96m', '\033[m')))  
        
        if opcaoMenu == '1':
            
            while True:
                print('\nVamos cadastrar seu novo livro')

                #ficha cadastral
                nomeLivro = str(input('{}Nome do livro:{} '.format('\033[96m', '\033[m')))
                editoraLivro = str(input('{}Nome da editora:{} '.format('\033[96m', '\033[m')))
                autorLivro = str(input('{}Nome do autor:{} '.format('\033[96m', '\033[m')))
                generoLivro = str(input('{}Genero do livro:{} '.format('\033[96m', '\033[m')))
                anoLivro = str(input('{}Ano do livro:{} '.format('\033[96m', '\033[m')))
                
                #validacao ISBN
                while True:
                    
                    isbnLivro = str(input('{}ISBN do livro:{} '.format('\033[36m', '\033[m')))

                    isbnLivro = isbnLivro.replace('-','') 	# remove -
                    isbnLivro = isbnLivro.replace(' ','') 	# remove espaco  
                    
                    #compilando regex
                    digito10 = re.compile(r'^\d{10}$') # 10 dígitos
                    digito10x = re.compile(r'^\d{9}X$') # 9 dígitos com X
                    digito13 = re.compile(r'^\d{13}$') # 13 dígitos

                    c = Counter(isbnLivro)
                    quantidade = list(c.values())[0]  # primeiro e talvez único valor da lista

                    
                    sucesso = '\n\033[32mISBN válido!\033[m\n'
                    falhou = '\n\033[31mISBN inválido!\033[m \nTente novamente\n'
                    
                    #numeros iguais
                    
                    if (quantidade == len(isbnLivro)) == True:# se a quantidade for igual, todos os itens são iguais.
                        print(falhou)       

                    #10 dígitos ISBN
                    elif digito10.match(isbnLivro) or digito10x.match(isbnLivro):
                        fator = len(isbnLivro)
                        total = 0
                        
                        for digit in isbnLivro:
                            if digit == 'X': 
                                digit = 10
                            total += (int(digit)*fator)
                            fator -= 1
                            
                        if total % 11 == 0 :
                            print(sucesso)
                            break
                        else:
                            print(falhou)


                    #13 dígito ISBN
                    elif digito13.match(isbnLivro):
                        total = 0
                        contador = 1
                        for digit in isbnLivro:
                            digit = int(digit)
                            if contador % 2 == 0:
                                digit = digit * 3
                            contador += 1
                            total += digit
                        if total % 10 == 0 :
                            print(sucesso)
                            break
                        else:
                            print(falhou)
                            
                    else:  #Nem 10 nem 13 digits
                        print(falhou)
                    
                
                livro = {
                    'nome': nomeLivro,
                    'editora': editoraLivro,
                    'autor': autorLivro,
                    'genero': generoLivro,
                    'ano': anoLivro,
                    'isbn': isbnLivro
                }
                
                livraria.append(livro)

                resp = ' '
                while resp not in 'SsNn':
                    resp = str(input('\033[96mDeseja cadastrar outro livro? S/N:\033[m '))
                    
                if resp in 'Nn':
                    break
            
        elif opcaoMenu == '2':
 
            # Verifica se a lista está vazia
            if len(livraria) == 0:
                
                print('\n\033[31mNão existem livros cadastrados.\033[m \nEscolha a opção 1 no Menu para cadastrar um livro')
            else:
                
                linha = '-' * 193

                print(linha)
                for label in livro:
                    print('|\033[32m {:^30}\033[m'.format(label.upper()), end='')
          
                print('|')
              
                print(linha)

                for indLis, campos in enumerate(livraria):
                  
                    for indDic in campos.values():
                        
                        print('| {:30}'.format(indDic [0:29]), end='')
                    
                    print('|')
                print(linha)
 
        elif opcaoMenu == '3':
            if len(livraria) == 0:
                
                print('\033[31mNão existem livros cadastrados.\033[m \nEscolha a opção 1 no Menu para cadastrar um livro')
            else:
                
                linha = '-' * 193

                print(linha)
                for label in livro:
                    print('|\033[32m {:^30}\033[m'.format(label.title()), end='')
          
                print('|')
              
                print(linha)

                for indLis, campos in enumerate(livraria):
                  
                    for indDic in campos.values():
                        
                        print('| {:30}'.format(indDic [0:29]), end='')
                    
                    print('|')
                print(linha)
              
            fim = False
            while fim != True:
                if len(livraria) == 0:
                    print("Não existem livros cadastrados.")
                    fim = True
                else:
                    deletado = 0
                    escolha = str(input("Digite o nome do livro para ser deletado: "))
                    for indLis, campos in enumerate(livraria): 
                        if livraria[indLis]['nome'] == escolha:
                            del livraria[indLis]
                            deletado += 1 
                        else:
                            fim = False
                    if deletado > 0:
                        print("Livro deletado com sucesso.")
                        teste = str(input("Deseja excluir outro livro [S] ou [N] ")).upper()
                        if teste == "S":
                            fim = False
                        else:
                            fim = True
                    else:
                        print("Livro não cadastrado.")
                    
            
        elif opcaoMenu == '4':
            print('\n\033[32mSistema finalizado com sucesso.\033[m\n')
            
        else:
            print('\n\033[31mOpcão inválida, tente novamente!\033[m\n')
         

