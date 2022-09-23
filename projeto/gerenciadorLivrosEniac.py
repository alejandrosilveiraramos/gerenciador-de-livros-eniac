










































































































































livraria = []

#cadastro = "S"
#while cadastro == "S":
while True:
    nome = str(input("Informe o Nome do livro: "))
    editora = str(input("Informe a Editora do livro: "))
    autor = str(input("Informe o Autor do livro: "))
    genero = str(input("Informe o Gênero do livro: "))
    ano = str(input("Informe o Ano de lançamento do livro: "))
    isbn = str(input("Informe o ISBN do livro: "))

    livro = {'Nome': nome,
          'Editora': editora,
          'Autor': autor,
          'Genero': genero,
          'Ano': ano,
          'ISBN': isbn}
    
    livraria.append(livro)

    cadastro = " "
    while cadastro not in "SN":
        cadastro = str(input("Deseja cadastrar outro livro? [ S ] ou [ N ]. ")).upper().strip()
    if cadastro == "n":
        break    

# Verifica se a lista está vazia
if len(livraria) == 0:
    # Imprime messagem de lista vazia
    print("Não ha livros cadastrado.")
else:
    # Decoração, cria um linha usando polimorfismo
    linha = "-" * 193

    # Imprime uma linha
    print(linha)
    # Estrutura de repetição para criar as labels da tabela
    for label in livro:
        # Imprime as labels com espaço de 30 caracteres e centralizado
        print(f"|\033[32m {label:^30}\033[m", end="")
    # Imprime um "|" no final da linha e cria a próxima linha
    print("|")
    # Imprime uma linha
    print(linha)
    # Estrutura de repetição onde "indLis" assume o valor do indice da lista
    # e "campos" assume os valores das Keys e Values.
    for indLis, campos in enumerate(livraria):
        # Estrutuda de repetição onde se imprime os dados do dicionário
        for indDic in campos.values():
            # imprime os dados do dicionário e formata para que não ultrapasse os 30 caracteres
            print("| {:30}".format(indDic [0:29]), end="")
        # Imprime um "|" no final da linha e cria a próxima linha
        print("|")
    # Imprime uma linha
    print(linha)
    print("teste")
=======
import re
from time import sleep


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
                    
                
                resp = ' '
                while resp not in 'SsNn':
                    resp = str(input('Deseja cadastrar outro livro? '))
                    
                if resp in 'Nn':
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









        
                 
              
    

