from access import logged, signin, login, users, DeleteUser
from shell import cria_arquivo, cria_dir, apaga_arquivo, apaga_dir, listar, extrair_caminho
import os
print('------ MINI SHELL ------\n')
if not users:
    signin()
else:
    login()

os.system('cls' if os.name == 'nt' else 'clear')

if logged != None:
    comando = None
    while comando != "fechar shell":
        comando = input()
        caminho = extrair_caminho(comando)
        if comando.startswith("criar arquivo"):
            cria_arquivo(caminho)
        elif comando.startswith("apagar arquivo"):  
            apaga_arquivo(caminho)
        elif comando.startswith("criar diretorio"):
            cria_dir(caminho)
        elif comando.startswith("apagar diretorio"):
            apaga_dir(caminho)
        elif comando == 'listar':
            listar()