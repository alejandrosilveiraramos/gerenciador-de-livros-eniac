import re


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


while True:
    print('Vamos cadastrar seu novo livro')

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

 producao-alejandro
        sucesso = 'ISBN valido!'
        falhou = 'ISBN não valido. \nTente novamente...'

        #10 dígitos ISBN
        if digito10.match(isbnLivro) or digito10x.match(isbnLivro):
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
            
    break

print('deu boa')

#4 finalizar o programa // MC vargas
from time import sleep

decoracao = '-=' * 5 

livraria = []
livro = {}

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
            print('1')
        elif opcaoMenu == 2:
            print('2')
        elif opcaoMenu == 3:
            print('3')
        elif opcaoMenu == 4:
            print('Programa Finalizado.')
        else:
            print('Opcão inválida\n')
            sleep(1) 




        
                 
              
    

