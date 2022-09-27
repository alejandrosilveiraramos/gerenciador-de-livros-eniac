livraria = []
livro = {}
tamanhoCampo = [8, 8, 8, 8, 8, 8]
espacoCampo = [8, 8, 8, 8, 8, 8]

"""
Na opção 04 tem o código modificado para faser a exclusão dos cadastro.
"""

opcao = "0"

while opcao != "5":
    try:
        
        print("""
        [ 1 ] => Opção 01
        [ 2 ] => Cadastrar
        [ 3 ] => Listar
        [ 4 ] => Deletar
        [ 5 ] => Sair...
        """)
        opcao = str(input("Qual a sua opção: "))

        # Teste ENTER para sair
        if opcao == "1":

            print("\nOpção 01")
            while True:
                sair = str( input( '\nPRESSIONE "ENTER" PARA SAIR ' ) )
                if not sair:
                    #exit()
                    print("Sair")
                    break   

        # Opção cadastro de livros
        elif opcao == "2":

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

        # Opção de listar os livros
        elif opcao == "3":

            if len(livraria) == 0:
                print("Não existem livros cadastrados.")
            else:
                # Calcula o tamanho de cada campo da tabela

                for x, y in enumerate(livraria):
                    cont = 0
                    for i in y.values():
                        if len(i) <= 6:
                            tamanhoCampo[cont] = 6
                            espacoCampo[cont] = 6
                        elif (len(i) > 6) and (len(i) < 30):
                            if len(i) > espacoCampo[cont]: 
                                tamanhoCampo[cont] = len(i)
                                espacoCampo[cont] = len(i)
                        elif len(i) >= 30:
                            tamanhoCampo[cont] = 30
                            espacoCampo[cont] = 30
                        cont += 1       

                linha ="-" * (sum(tamanhoCampo) + 7 + 12)
                print(linha)
                cont = 0
                for label in livro:
                    print(f"| {label[0:espacoCampo[cont]]:^{tamanhoCampo[cont]}} ", end="")
                    cont += 1
                print("|")
                print(linha)

                for indLis, campos in enumerate(livraria):
                    cont = 0
                    for indDic in campos.values():
                        print(f"| {indDic[0:espacoCampo[cont]]:{tamanhoCampo[cont]}} ", end="")
                        cont +=1
                    print("|")
                print(linha)

        # Opção excluir livros
        elif opcao == "4":

            fim = False
            while fim != True:
                if len(livraria) == 0:
                    print("Não existem livros cadastrados.")
                    fim = True
                else:
                    deletado = 0
                    escolha = str(input("Digite o nome do livro para ser deletado: "))
                    for indLis, campos in enumerate(livraria): 
                        if livraria[indLis]['Nome'] == escolha:
                            del livraria[indLis]
                            deletado += 1 
                        else:
                            fim = False
                    if deletado > 0:
                        print("Livro deletado com sucesso.")
                        teste = str(input("Deseja excluir outro livro [S] ou [N] ")).upper()
                        if teste == "S":
                            fim = False
                        else:
                            fim = True
                    else:
                        print("Livro não cadastrado.")

        # Opção para sair di programa
        elif opcao == "5":
            print("\nSair")
            
        else:
            print("\nOpção inválida. Tente novamente.")

    except ValueError:
        print("\nOops! Esse não é um número válido. Tente novamente...")

print("\nFim do programa.")