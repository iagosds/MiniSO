class User:
    def __init__(self, name, password):
        self._name = name
        self.__password__ = password # Senha deve ser salva utilizando um salt hash

users = {}



        