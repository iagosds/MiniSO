from user import users
from access import logged, signin, login, DeleteUser
from shell import cria_arquivo, cria_dir, apaga_arquivo, apaga_dir, listar, extrair_caminho
import os

# 1. Caso não exista nenhum usuário cadastrado no MiniSO, será solicitado no shell,
#  a criação de um usuário e com senha. A senha deve ser salva utilizando um salt e em hash (SHA-512),
#  como foi feito no exercício de segurança.

# 2. Caso haja pelo menos 1 usuário cadastrado, o shell solicitará usuário e senha para login.
#  A senha não deve aparecer enquanto o usuário a digita! (Pode ficar com asteriscos ou sem nada no lugar)

if not users:
    logged = signin()
else:
    logged = login()

os.system('cls')

if logged is not None:
    comando = None
    print('------ MINI SHELL ------')
    while comando != "fechar shell":
        comando = input()
        caminho = extrair_caminho(comando)
        if comando.startswith("criar arquivo"):
            cria_arquivo(caminho, logged)
        elif comando.startswith("apagar arquivo"):  
            apaga_arquivo(caminho, logged)
        elif comando.startswith("criar diretorio"):
            cria_dir(caminho)
        elif comando.startswith("apagar diretorio"):
            apaga_dir(caminho)
        elif comando == 'listar':
            listar()
        elif comando == f'deletar usuario {logged}':
            logged = DeleteUser()