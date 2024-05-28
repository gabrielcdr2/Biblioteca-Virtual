import functions

users = [
    {"login": "admin", "password": "admin", "acess": "administrator"},
    {"login": "Gabriel", "password": "2004", "acess": "comum"},
    {"login": "albert123", "password": "1968", "acess": "comum"},
    {"login": "bibliotecaria", "password": "123", "acess": "bibliotecária"},

]

def main():
    validation = functions.login(users) # 
    while True:
        if validation == "administrator":
            print('Você é um ', validation)
            break
        
if __name__ == "__main__":
    main()