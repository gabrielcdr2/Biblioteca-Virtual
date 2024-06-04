import functions

users = [
    {"login": "admin", "password": "admin", "acess": "administrator"},
    {"login": "Gabriel", "password": "2004", "acess": "comum"},
    {"login": "albert123", "password": "1968", "acess": "comum"},
    {"login": "bibliotecaria", "password": "123", "acess": "bibliotecária"},
]

livros_reservados = []
livros_cadastrados = ["Direito", "Engenharia de Software","Introdução a Computadores","Analise de Requisitos"] 

def main():
    validation = functions.login(users) 

    while True:
        if validation == "administrator":
            while True:
                print('')
                print("-"*25)
                print(f'{"Biblioteca Virtual:":^25} ')
                print("-"*25)
                print("1 - Pesquisar Livros")
                print("2 - Livros Reservados ")
                print("3 - Cancelar Reserva")
                print("4 - Gerenciar Usuários")
                print("5 - Sair\n")

                selecao = input("Selecione uma das opções acima: ")

                try:
                    int(selecao)
                    if int(selecao) > 5:
                        print('Digite somente as opções válidas.')
                        continue

                except ValueError:
                    print('Digite somente as opções validas.')
                    continue
                
                if  selecao == "1":
                    print("-"*25)
                    print(f'{"Pesquisar Livros":^25}')
                    print("-"*25)
                    
                    while True:
                        pesquisa = input("Digite o nome do Livro: ").lower()
                        disponibilidade = functions.verificar_disponibilidade(pesquisa, livros_cadastrados)

                        if disponibilidade == -1:
                            print('Livro não encontrado!')
                            continue
                        
                        else:
                            reservar = input("O livro foi encontrado. Deseja reservar o livro? [S/N] ").lower()
                            if reservar == "s":
                                livros_reservados.append(pesquisa)
                                print("Livro reservado!")
                                break
                
                
                elif selecao == "2":
                    print("-"*25)
                    print(f'{"Livros Reservados:":^25}')
                    print("-"*25)
                    for livros in livros_reservados:
                        print('-',livros)
                    print('''''')

                elif selecao == "3":
                    cancelar_reserva = input("Digite o nome do livro que deseja cancelar a reserva: ")
                    if cancelar_reserva.lower() in livros_reservados:
                        livros_reservados.remove(cancelar_reserva)
                        print('Reserva cancelada.')

                elif selecao == "4":
                    functions.gerenciar_usuarios(users)
                
                elif selecao == "5":
                    break

        elif validation == 'bibliotecária':
            while True:
                print("-"*25)
                print(f'{"Biblioteca Virtual:":^25} ')
                print("-"*25)
                print("1 - Pesquisar Livros")
                print("2 - Gerenciar Livros")
                print("3 - Sair\n")

                selecao = input("Selecione uma das opções acima: ")
                
                if  selecao == "1":
                    print("-"*25)
                    print(f'{"Pesquisar Livros":^25}')
                    print("-"*25)

                    pesquisa = input("Digite o nome do Livro: ")

                    verificar = functions.verificar_disponibilidade(pesquisa, livros_cadastrados)

                    if verificar == -1:
                        print('Livro não encontrado.')

                    else:
                        reservar = input("O livro foi encontrado. Deseja reservar o livro? [S/N] ").lower()
                        if reservar == "s":
                            livros_reservados.append(pesquisa)
                            print("Livro reservado!")

                elif selecao == "2":
                    functions.gerenciar_livros(livros_cadastrados)

                elif selecao == "3":
                    print("Obrigado por usar a nossa biblioteca!")
                    break

        else:
            while True:
                print("-"*25)
                print(f'{"Biblioteca Virtual:":^25} ')
                print("-"*25)
                print("1 - Pesquisar Livros")
                print("2 - Livros Reservados")
                print("3 - Cancelar reserva")
                print("4 - Sair\n")

                selecao = input("Selecione uma das opções acima: ")
                
                if  selecao == "1":
                    print("-"*25)
                    print(f'{"Pesquisar Livros":^25}')
                    print("-"*25)

                    pesquisa = input("Digite o nome do Livro: ")

                    verificar = functions.verificar_disponibilidade(pesquisa, livros_cadastrados)

                    if verificar == -1:
                        print('Livro não encontrado.')

                    else:
                        reservar = input("O livro foi encontrado. Deseja reservar o livro? [S/N] ").lower()
                        if reservar == "s":
                            livros_reservados.append(pesquisa)
                            print("Livro reservado!")
                
                elif selecao == "2":
                    print("-"*25)
                    print(f'{"Livros Reservados:":^25}')
                    print("-"*25)
                    for livros in livros_reservados:
                        print('-',livros)
                    print('''''')
                elif selecao == "3":
                    cancelar_reserva = input("Digite o nome do livro que deseja cancelar a reserva: ")
                    if cancelar_reserva in livros_reservados:
                        livros_reservados.remove(cancelar_reserva)
                elif selecao == "4":
                    break

if __name__ == "__main__":
    main()
    