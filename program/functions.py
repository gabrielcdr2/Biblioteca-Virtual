import os, time

# Login validation function
def login(dictionary):
    while True: # Create a loop for continue showing the login screen until the user enter valid informations 
        print('='*20)
        print('Bilioteca Virtual')
        print('='*20)
        login = input('Login: ')
        password = input('Senha: ')
        
        i = 0
        for item in dictionary:
            if login == item["login"]:
                if password == item["password"]:
                    os.system("cls") # cleans the terminal
                    return item["acess"]
                else:
                    print('Senha incorreta!')
                    time.sleep(2)
                    os.system("cls") # cleans the terminal
                    break
            else:
                i += 1
            if i >= len(dictionary):
                print('Usuário incorreto.')
                time.sleep(2)
                os.system("cls") # cleans the terminal
                break

# Funções do Administrador

# Pesquisar Livros
def verificar_disponibilidade(pesquisa, livros_cadastrados):
    livros_cadastrados.sort()
    inicio, fim = 0, len(livros_cadastrados) - 1

    while inicio <= fim:
        meio = (inicio+fim)//2

        if livros_cadastrados[meio].lower() == pesquisa:
            return meio
        elif livros_cadastrados[meio].lower() < pesquisa:
            inicio = meio + 1
        else:
            fim = meio - 1            
    
    return -1

# Gerenciador de usuários
def gerenciar_usuarios(users):
    while True:
        print("\n1 - Cadastrar Usuários")
        print("2 - Deletar Usuários")
        print("3 - Listar Usuários")
        print("4 - Voltar ao início")

        selecao = input("Selecione uma das opções acima: ")

        try:
            int(selecao)
            if int(selecao) > 4:
                print('Digite somente as opções válidas.')
                continue

        except ValueError:
            print('Digite somente as opções validas.')
            continue
        
        if selecao == "1":
            cadastrar_usuario(users)

        elif selecao == "2":
            deletar = input("\nDigite o usuário que deseja deletar: ")
            deletou = False

            for usuario in users:
                if deletar == usuario["login"]:
                    users.remove(usuario)
                    print("Usuário deletado.")
                    deletou = True
                    break

            if not deletou:
                print('Usuario não encontrado.')
                break

        elif selecao == "3":
            print("\nLista de Usuários:")
            for usuario in users:
                print(usuario["login"], usuario["acess"])
        elif selecao == "4":
            break

# Cadastrar os usuários
def cadastrar_usuario(users):
    while True:
        print("-"*25)
        print(f'{"Cadastro de usuários":^25}')
        print("-"*25)

        login = input("login: ")
        senha = input("Senha: ")
        acesso = input("Acesso: ")

        for user in users:
            if login == user["login"]:
                print('Usuario já existente.')
                continue

        users.append({"login":login, "password":senha, "acess":acesso})
        print('Usuário cadastrado!')
        criar_log(users, login)
        break

# Gerenciar livros
def gerenciar_livros(livros_cadastrados):
    while True:
        print("-"*27)
        print(f'{"Gerenciamento de Livros":^27}')
        print("-"*27)
        print("1 - Adicionar Livro ")
        print("2 - Remover Livros ")
        print("3 - Listar Livros ")
        print("4 - Voltar a Pagina Inicial")
        Escolha = input("\nEscolha uma das alternativas: ")
     
        if Escolha == "1": 
            print("-"*25)
            print("Tela de Adicionar Livro")
            print("-"*25)
            titulo = input("Digite o Titulo: ")
            print("-"*25)
            autor = input("Digite o Nome Autor: ")
            print("-"*25)
            data_de_lançamento = input("Digite a Data de Lançamento: ")
            print("-"*25)
            print("Livro Cadastrado!!")
            print("-"*25)
            livros_cadastrados.append(titulo)
        
        elif Escolha == "2": 
            Nome_do_livro_remover = input("Digite o nome do Livro que vc quer Remover: ")
            if Nome_do_livro_remover in livros_cadastrados:
                livros_cadastrados.remove(Nome_do_livro_remover)
            
        
        elif Escolha == "3":
            print("-"*25)
            print(f'{"Lista de livros:":^25}')
            print("-"*25)
            for livros in livros_cadastrados:
                print('-',livros)
        elif Escolha == "4": 
            break
        
        else: 
            print("escolha uma opção válida")

        # Gerenciar livros
def gerenciar_livros(livros_cadastrados):
    while True:
        print("-"*27)
        print(f'{"Gerenciamento de Livros":^27}')
        print("-"*27)
        print("1 - Adicionar Livro ")
        print("2 - Remover Livros ")
        print("3 - Listar Livros ")
        print("4 - Voltar a Pagina Inicial")
        Escolha = input("\nEscolha uma das alternativas: ")
     
        if Escolha == "1": 
            print("-"*25)
            print("Tela de Adicionar Livro")
            print("-"*25)
            titulo = input("Digite o Titulo: ")
            print("-"*25)
            autor = input("Digite o Nome Autor: ")
            print("-"*25)
            data_de_lançamento = input("Digite a Data de Lançamento: ")
            print("-"*25)
            print("Livro Cadastrado!!")
            print("-"*25)
            livros_cadastrados.append(titulo)
        
        elif Escolha == "2": 
            Nome_do_livro_remover = input("Digite o nome do Livro que vc quer Remover: ")
            if Nome_do_livro_remover in livros_cadastrados:
                livros_cadastrados.remove(Nome_do_livro_remover)
            
        
        elif Escolha == "3":
            print("-"*25)
            print(f'{"Lista de livros:":^25}')
            print("-"*25)
            for livros in livros_cadastrados:
                print('-',livros)
        elif Escolha == "4": 
            break
        
        else: 
            print("escolha uma opção válida")

def criar_log(users, nome):
    with open('log', 'w') as log:
        log.write(f"O usuario {nome} foi adicionado ao sistema!")