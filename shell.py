import os
import string
import re
from processos import cria_processo
from dir import Dir, dirs

def extrair_caminho(comando):
    padrao = r"^(criar|apagar) (diretorio|arquivo) (.+)$"
    match = re.match(padrao, comando.strip(), re.IGNORECASE)
    if match:
        return match.group(3).strip()
    return None

################################


def cria_arquivo(caminho_arquivo, logged):
    if cria_processo():
        if '/' in caminho_arquivo:
            dir_path = os.path.dirname(caminho_arquivo)
            if not os.path.exists(dir_path):
                print(f'Diretório não existe, rode o comando: "criar diretorio {os.path}"')
                
        else:
            # O arquivo será criado no diretório corrente
            dir = Dir(caminho_arquivo, logged, 'file')
            dirs[caminho_arquivo] = dir
            dir_path = os.getcwd()
            caminho_arquivo = os.path.join(dir_path, caminho_arquivo)
        with open(caminho_arquivo, 'w') as f:
            pass


def apaga_arquivo(caminho_arquivo, logged):
    if os.path.isfile(caminho_arquivo) and caminho_arquivo in dirs:
        print(logged, dirs[caminho_arquivo].owner)
        if logged == dirs[caminho_arquivo].owner:
            if cria_processo():
                   os.remove(caminho_arquivo)
                   del dirs[caminho_arquivo]
        else:
            print("Usuário não tem permissão para acessar esse arquivo")
    else:
        print('O arquivo não existe.')


def cria_dir(caminho_dir):
    if cria_processo():
        if '/' in caminho_dir:
            dir_path = os.path.dirname(caminho_dir)
            if not os.path.exists(dir_path):
                caminho = os.path.join(dir_path, caminho_dir)
                os.makedirs(caminho)
        else:
            # O arquivo será criado no diretório corrente
            dir_path = os.getcwd()
            caminho = os.path.join(dir_path, caminho_dir)
            os.makedirs(caminho)

def apaga_dir(caminho_dir):
    if cria_processo():
        if os.path.isdir(caminho_dir):
            try:
                os.rmdir(caminho_dir)
            except:
                print('O diretório não existe ou não está vazio')
    
def listar():
    print(dirs)
    if cria_processo():
        for i in os.listdir(os.getcwd()):
            print('\t', i)
    

