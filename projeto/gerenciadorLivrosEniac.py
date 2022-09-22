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

while True:
    print('Vamos cadastrar seu novo livro')

    '''nomeLivro = str(input('Nome do livro: '))
    editoraLivro = str(input('Nome da editora: '))
    autorLivro = str(input('Nome do autor: '))
    generoLivro = str(input('Genero do livro: '))
    anoLivro = str(input('Ano do livro: '))'''
    isbnLivro = str(input('ISBN do livro: '))

    isbnLivro = isbnLivro.replace("-","") 	# remove -
    isbnLivro = isbnLivro.replace(" ","") 	# remove whitespace

    #complile regex expressions
    type10 = re.compile(r"^\d{10}$") # 10 digit
    type10x = re.compile(r"^\d{9}X$") # 9 digit with X
    type13 = re.compile(r"^\d{13}$") # 13 digit

    success = "ISBNLisbnLivro is valid!"
    fail = "ISBNLisbnLivro is invalid."

    #10 digit ISBNLisbnLivro logic
    if type10.match(isbnLivro) or type10x.match(isbnLivro):
        factor = len(isbnLivro)
        total = 0
        for digit in isbnLivro:
            if digit == "X": 
                digit = 10
            total += (int(digit)*factor)
            factor -= 1
        if total % 11 == 0 :
            print('success')
        else:
            print("fail")

    #13 digit ISBNLisbnLivro logic
    elif type13.match(isbnLivro):
        total = 0
        counter = 1
        for digit in isbnLivro:
            digit = int(digit)
            if counter % 2 == 0:
                digit = digit * 3
            counter += 1
            total += digit
        if total % 10 == 0 :
            print ('success')
        else:
            print("fail")
    else:  #neither 10 nor 13 digits
        print("fail")

