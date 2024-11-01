class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __repr__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}')"
