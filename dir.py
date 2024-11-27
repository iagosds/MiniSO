class Dir:
    def __init__(self, nome, owner, type):
        self.nome = nome
        self._owner = owner
        self.type = type
    @property
    def owner(self):
        return self._owner

dirs = {}