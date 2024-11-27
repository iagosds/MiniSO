from user import User, users
import hashlib
import os

def CreateSalt():
    return os.urandom(10).hex()

def CreateHash(senha, salt):
    senha_salt = salt + senha
    return hashlib.sha512(senha_salt.encode()).hexdigest()

logged = None
# 1. Caso não exista nenhum usuário cadastrado no MiniSO, será solicitado no shell, a criação de um usuário e com senha. A senha deve ser salva utilizando um salt e em hash (SHA-512), como foi feito no exercício de segurança.
def signin(logged = logged):
    name = input('Digite o nome do usuário: ')
    if name in users:
        print('Nome já está em uso')
        login()
    else:
        password = input('Digite a senha: ') # Não mostrar digitação
        salt = CreateSalt()
        password = CreateHash(password, salt)
        users[name] = salt, password
        logged = name
        print('Usuário criado e logado!')
        return logged

def login(logged = logged):
    name = input('Digite o nome do usuário: ')
    if name not in users:
        print('Usuário não cadastrado')
        return
    salt, senha_hash = users[name]
    senha = input('Digite a senha: ') # Não mostrar digitação
    if CreateHash(senha, salt) == senha_hash:
        logged = name
        return logged




# 2. Caso haja pelo menos 1 usuário cadastrado, o shell solicitará usuário e senha para login. A senha não deve aparecer enquanto o usuário a digita! (Pode ficar com asteriscos ou sem nada no lugar)
# def menu():
#     while True:
#         print("\n1. Cadastrar novo usuário")
#         print("2. Fazer login")
#         print("3. Sair")
        
#         opcao = input("Escolha uma opção: ")
#         if opcao == '1':
#             signin()
#         elif opcao == '2':
#             login()
#         elif opcao == '3':
#             print("Saindo...")
#             break
#         else:
#             print("Opção inválida, tente novamente.")
# if not users:
#     signin()
# else:
#     login()


# 3. Caso o último usuário do MiniSO seja excluído, deve ser executado o passo 1 assim que ele seja apagado e para cada nova execução
def DeleteUser(logge = logged):
    salt, senha_hash = users[logged]
    senha = input(f"Digite a senha do usuário {logged}: ")
    if CreateHash(senha, salt) == senha_hash:
        del users[logged]
        logged = None
        signin()
        return logged