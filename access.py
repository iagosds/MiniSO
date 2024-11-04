from user import User, users

# 1. Caso não exista nenhum usuário cadastrado no MiniSO, será solicitado no shell, a criação de um usuário e com senha. A senha deve ser salva utilizando um salt e em hash (SHA-512), como foi feito no exercício de segurança.
def login():
    name = input('Digite o nome do usuário: ')
    for user in users:
        if user.name == name:
            print('Nome já está em uso')
            login()
        else:
            password = input('Digite a senha: ')
            user = User(name, password)
            users.append(user)
            break

def signin(name):
    for user in users:
        if user.name == name:
            senha = input('Digite a senha: ')
            if senha == user.password:
                # Acessar shell
                pass
            else:
                print('Senha incorreta!')
                signin()


if len(users) == 0:
    login()

# 2. Caso haja pelo menos 1 usuário cadastrado, o shell solicitará usuário e senha para login. A senha não deve aparecer enquanto o usuário a digita! (Pode ficar com asteriscos ou sem nada no lugar)
else:
    signin(namex)


# 3. Caso o último usuário do MiniSO seja excluído, deve ser executado o passo 1 assim que ele seja apagado e para cada nova execução