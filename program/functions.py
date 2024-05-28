import os, time

users = [
    {"login": "admin", "password": "admin", "acess": "administrator"}
]

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
