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
print(decoracao, 'GERENCIADOR DE LIVROS ENIAC', decoracao)
while opcaoMenu != 4:
        
        sleep(1.1)
        opcaoMenu = int(input('''Menu \nEscolha uma das opções abaixo: \n
1 -> Cadastrar Livro
2 -> Listar Livros
3 -> Excluir Livros
4 -> Encerrar o programa\n
Qual opção: '''))  
        if opcaoMenu == 1:
            
            while True:
                print('\nVamos cadastrar seu novo livro:\n')

                #ficha cadastral
                nomeLivro = str(input('Nome do livro: '))
                editoraLivro = str(input('Nome da editora: '))
                autorLivro = str(input('Nome do autor: '))
                generoLivro = str(input('Genero do livro: '))
                anoLivro = str(input('Ano do livro: '))
                
                #validacao ISBN
                while True:
                    
                    isbnLivro = str(input('ISBN do livro: '))

                    isbnLivro = isbnLivro.replace('-','') 	# remove -
                    isbnLivro = isbnLivro.replace(' ','') 	# remove espaco  
                    
                    #compilando regex
                    digito10 = re.compile(r'^\d{10}$') # 10 dígitos
                    digito10x = re.compile(r'^\d{9}X$') # 9 dígitos com X
                    digito13 = re.compile(r'^\d{13}$') # 13 dígitos

                    c = Counter(isbnLivro)
                    quantidade = list(c.values())[0]  # primeiro e talvez único valor da lista

                    
                    sucesso = '\nISBN valido!\n'
                    falhou = '\nISBN não valido. \nTente novamente...\n'
                    
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
                    resp = str(input('Deseja cadastrar outro livro? S/N '))
                    
                if resp in 'Nn':
                    break
            
        elif opcaoMenu == 2:
 
            # Verifica se a lista está vazia
            if len(livraria) == 0:
                
                print("\nNão ha livros cadastrado.")
            else:
                
                linha = "-" * 193

                print(linha)
                for label in livro:
                    print(f"|\033[32m {label:^30}\033[m", end="")
          
                print("|")
              
                print(linha)

                for indLis, campos in enumerate(livraria):
                  
                    for indDic in campos.values():
                        
                        print("| {:30}".format(indDic [0:29]), end="")
                    
                    print("|")
                print(linha)
 
        elif opcaoMenu == 3:
            print('\nLista de Livros Cadastrados')
            if len(livraria) == 0:
                
                print("Não ha livros cadastrado.")
            else:
                
                linha = "-" * 193

                print(linha)
                for label in livro:
                    print(f"|\033[32m {label:^30}\033[m", end="")
          
                print("|")
              
                print(linha)

                for indLis, campos in enumerate(livraria):
                  
                    for indDic in campos.values():
                        
                        print("| {:30}".format(indDic [0:29]), end="")
                    
                    print("|")
                print(linha)

            escolha = str(input('Qual livro deseja apagar? '))

            for i in range(len(livraria)):
                if livraria[i]['nome'] == escolha:
                    del livraria[i]
                    break

            print('\nLivro deletado com sucesso!\n')
            
        elif opcaoMenu == 4:
            print("\nSistema finalizado com sucesso.\n")
            
        else:
            print('Opcão inválida, tente novamente!')
         