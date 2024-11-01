from datetime import datetime

class Amizade:
    def __init__(self, usuario1_id, usuario2_id, data_inicio):
        self.usuario1_id = usuario1_id
        self.usuario2_id = usuario2_id
        self.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')

    def __repr__(self):
        return f"Amizade({self.usuario1_id}, {self.usuario2_id}, {self.data_inicio.date()})"
