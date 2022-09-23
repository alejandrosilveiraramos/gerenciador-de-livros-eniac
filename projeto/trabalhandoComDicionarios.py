livraria = []

cadastro = "S"
while cadastro == "S":
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

    cadastro = str(input("Deseja cadastrar outro livro? [ S ] ou [ N ]. ")).upper().strip()

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