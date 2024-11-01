from datetime import datetime


class Mensagem:
    def __init__(self, remetente_id, destinatario_id, data, conteudo):
        self.remetente_id = remetente_id
        self.destinatario_id = destinatario_id
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.conteudo = conteudo

    def __repr__(self):
        return f"Mensagem(de={self.remetente_id}, para={self.destinatario_id}, data={self.data.date()})"
