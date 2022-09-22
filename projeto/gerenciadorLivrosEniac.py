print('\nLista de Livros Cadastrados')
cont = 0
print('-' * 30)
for livro in lista_livros:
    cont += 1
    print('Livro ', cont, livro["nome"])
    print('\n', 'Nome: ', livro["nome"], '\n', 'Ano: ', livro["ano"], '\n', 'Autor: ', livro["autor"], '\n', 'ISBN: ', livro["ISBN"])
    print('-' * 30)

escolha = int(input('Qual livro deseja apagar ? '))

if escolha != lista_livros:
    print("Esta opção não existe")
else:
    lista_livros.pop(escolha - 1)
    print('=' * 30)
    print('\nLivro Deletado\n')
    print('=' * 30)