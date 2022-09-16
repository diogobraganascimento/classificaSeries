class Serie:
    def __init__(self, nome, categoria, plataforma, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha