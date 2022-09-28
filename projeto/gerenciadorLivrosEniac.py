
import re
from collections import Counter
from time import sleep

livraria = []
livro = {}
tamanhoCampo = [8, 8, 8, 8, 8, 8]
espacoCampo = [8, 8, 8, 8, 8, 8]

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
                    if resp not in 'SsNn':
                        print('\n\033[31mOpção inválida!\033[m \nTente novamente\n')
                    
                if resp in 'Nn':
                    break
            
        elif opcaoMenu == '2':
 
            if len(livraria) == 0:
                print('\033[31mNão existem livros cadastrados.\033[m \nEscolha a opção 1 no Menu para cadastrar um livro')
            else:
                # Calcula o tamanho de cada campo da tabela

                for x, y in enumerate(livraria):
                    cont = 0
                    for i in y.values():
                        if len(i) <= 6:
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        elif (len(i) > 6) and (len(i) < 30):
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        elif len(i) >= 30:
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        cont += 1       

                linha ='-' * (sum(tamanhoCampo) + 7 + 12)
                print(linha)
                cont = 0
                for label in livro:
                    print(f'| \033[32m{label.upper()[0:espacoCampo[cont]]:^{tamanhoCampo[cont]}}\033[m ', end='')
                    cont += 1
                print('|')
                print(linha)

                for indLis, campos in enumerate(livraria):
                    cont = 0
                    for indDic in campos.values():
                        print(f'| {indDic[0:espacoCampo[cont]]:{tamanhoCampo[cont]}} ', end='')
                        cont +=1
                    print('|')
                print(linha)

 
        elif opcaoMenu == '3':
            if len(livraria) == 0:
                print('\n\033[31mNenhum livro cadastrado.\033[m\n\nEscolha a opção 1 \033[96m-> Cadastrar Livro\033[m no Menu para cadastrar um livro')
            else:
                # Calcula o tamanho de cada campo da tabela

                for x, y in enumerate(livraria):
                    cont = 0
                    for i in y.values():
                        if len(i) <= 6:
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        elif (len(i) > 6) and (len(i) < 30):
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        elif len(i) >= 30:
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        cont += 1       

                linha ='-' * (sum(tamanhoCampo) + 7 + 12)
                print(linha)
                cont = 0
                for label in livro:
                    print(f'| \033[32m{label.upper()[0:espacoCampo[cont]]:^{tamanhoCampo[cont]}}\033[m ', end='')
                    cont += 1
                print('|')
                print(linha)

                for indLis, campos in enumerate(livraria):
                    cont = 0
                    for indDic in campos.values():
                        print(f'| {indDic[0:espacoCampo[cont]]:{tamanhoCampo[cont]}} ', end='')
                        cont +=1
                    print('|')
                print(linha)
              
            acaoDeletar = False
            while acaoDeletar != True:
                if len(livraria) == 0:
                    acaoDeletar = True
                else:
                    deletado = 0
                    escolha = str(input('\n\033[96mDigite o nome do livro para ser deletado: \033[m'))
                    for indLis, campos in enumerate(livraria): 
                        if livraria[indLis]['nome'] == escolha:
                            del livraria[indLis]
                            deletado += 1 
                        else:
                            acaoDeletar = False
                            
                    if deletado > 0:
                        print('\n\033[32mLivro deletado com sucesso.\033[m\n')        
                        resp = ' '
                    elif deletado == 0:
                        print('\n\033[31mNão existe livro cadastrado com esse nome.\033[m')
                        acaoDeletar = False
                        
                    while resp not in 'SsNn':
                        resp = str(input('\033[96mDeseja deletar outro livro? S/N: \033[m'))
                        if resp not in 'SsNn':
                            print('\n\033[31mOpção inválida!\033[m \nTente novamente\n')  
                             
                    if resp in 'Ss':
                        acaoDeletar = False
                    elif resp in 'Nn':
                        acaoDeletar = True

                    if len(livraria) == 0:
                        print('\n\033[31mNenhum livro cadastrado.\033[m\n\nEscolha a opção 1 \033[96m-> Cadastrar Livro\033[m no Menu para cadastrar um livro') 

            
        elif opcaoMenu == '4':
            print('\n\033[32mSistema finalizado com sucesso.\033[m\n')
            
        else:
            print('\n\033[31mOpcão inválida, tente novamente!\033[m\n')
         

'''
isnb válido para teste
978-0-306-40615-7    13 digitos
99921-58-10-7        10 digitos
0-8044-2957-X        9+X
'''