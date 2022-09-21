listaLivros = []
#livros = {}

cadastro = "S"
while cadastro == "S":
    #livros.clear()
    nome = str(input("Informe o Nome do livro: "))
    editora = str(input("Informe a Editora do livro: "))
    autor = str(input("Informe o Autor do livro: "))
    genero = str(input("Informe o Gênero do livro: "))
    ano = str(input("Informe o Ano de lançamento do livro: "))
    isbn = str(input("Informe o ISBN do livro: "))

    livros = {'Nome': nome,
          'Editora': editora,
          'Autor': autor,
          'Genero': genero,
          'Ano': ano,
          'ISBN': isbn}
    
    #listaLivros.append(livros.copy())
    listaLivros.append(livros)

    cadastro = str(input("Deseja cadastrar outro livro? [ S ] ou [ N ]. ")).upper().strip()

print(listaLivros[0]['Autor'])
print(livros)


# Imprime o cabeçalho da tabela
print("-" * 187)
# Imprime as Labels
print("|{:30}|{:30}|{:30}|{:30}|{:30}|{:30}|".format(" Nome", " Editora", " Autor", " Genero", " Ano", " ISBN"))
print("-" * 187)
# Laço de repetição para percorrer a lista [listaLivros]
for i in listaLivros:
    # Laço de repetição para percorrer o dicionário [livros]  
    # Imprime a tabela com os dados do livro
    print("|{:30}|{:30}|{:30}|{:30}|{:30}|{:30}".format(i['Nome'], i['Editora'], i['Autor'], i['Genero'], i['Ano'], i['ISBN']), end="")
        # Imprime um "|" no final da linha e cria a próxima linha
    print("|")
# Imprime a linha final da tabela
print("-" * 187)