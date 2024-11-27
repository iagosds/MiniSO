from user import User, users
import hashlib
import os

def CreateSalt():
    return os.urandom(10).hex()

def CreateHash(senha, salt):
    senha_salt = salt + senha
    return hashlib.sha512(senha_salt.encode()).hexdigest()

logged = None
def signin():
    global logged
    print('----Sign In----')
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

def login():
    global logged
    print('----Login----')
    name = input('Digite o nome do usuário: ')
    if name not in users:
        print('Usuário não cadastrado')
        return
    salt, senha_hash = users[name]
    senha = input('Digite a senha: ') # Não mostrar digitação
    if CreateHash(senha, salt) == senha_hash:
        logged = name
        return logged
    else:
        print('Senha incorreta!')
        return None


# 3. Caso o último usuário do MiniSO seja excluído, deve ser executado o passo 1 assim que ele seja apagado e para cada nova execução
def DeleteUser():
    global logged
    salt, senha_hash = users[logged]
    senha = input(f"Digite a senha do usuário {logged}: ")
    if CreateHash(senha, salt) == senha_hash:
        del users[logged]
        print(f'Usuário {logged} digitado com sucesso.')
        logged = None
        signin()
        return logged
    else:
        print('Senha incorreta, usuário não foi deletado')
        return logged