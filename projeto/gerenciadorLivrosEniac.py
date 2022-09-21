# Dev

'''
Opção criar livro:

    - O programa deve perguntar as informações cadastrais, fazer a verificação do isbnLivro e, caso esteja tudo nos conformes,

    adicionar o livro mostrando uma mensagem de sucesso;

    - Caso tenha algum problema com o ISBN, o código deverá mostrar uma mensagem de erro e não cadastrar o livro, mostrando

    o menu novamente;

    - Os dados cadastrais do livro constam nos requisitos abaixo;
'''

import re


while True:
    print('Vamos cadastrar seu novo livro')

    '''nomeLivro = str(input('Nome do livro: '))
    editoraLivro = str(input('Nome da editora: '))
    autorLivro = str(input('Nome do autor: '))
    generoLivro = str(input('Genero do livro: '))
    anoLivro = str(input('Ano do livro: '))'''
    isbnLivro = str(input('ISBN do livro: '))

    while True:
       
        isbnLivro = isbnLivro.replace("-", "").replace(" ", "").upper();
        match = re.search(r'^(\d{9})(\d|X)$', isbnLivro)
        if not match:
            print('deuruim')
    
        digits = match.group(1)
        check_digit = 10 if match.group(2) == 'X' else int(match.group(2))

        result = sum((i + 1) * int(digit) for i, digit in enumerate(digits))
        if (result % 11) == check_digit:
            print('deuboa')
            break
