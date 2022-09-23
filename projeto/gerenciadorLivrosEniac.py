import re

# Dev

'''
Opção criar livro:

    - O programa deve perguntar as informações cadastrais, fazer a verificação do isbnLivroLivro e, caso esteja tudo nos conformes,

    adicionar o livro mostrando uma mensagem de sucesso;

    - Caso tenha algum problema com o ISBN, o código deverá mostrar uma mensagem de erro e não cadastrar o livro, mostrando

    o menu novamente;

    - Os dados cadastrais do livro constam nos requisitos abaixo;
'''

livro = '''                                                                
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
      '''
print(livro.center(50))

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