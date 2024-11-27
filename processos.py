from uuid import uuid1

class Processo:
    def __init__(self, tamanho):
        self.id = uuid1()
        self.tamanho = tamanho

memoria = [5, 4, 3, 2, 3, 4, 5]

def firstFit(processo, memoria=memoria):
    for idx, espaco in enumerate(memoria):
        if espaco>=processo.tamanho:
            memoria[idx] -= processo.tamanho
            return True
    return False

def cria_processo(memoria = memoria):
    process = Processo(2)
    print(process.id)
    if firstFit(process):
        return True
    else:
        print('Memória insuficiente')
        return False
    

