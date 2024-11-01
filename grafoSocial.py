# grafoSocial.py

from datetime import datetime
import matplotlib.pyplot as plt
import networkx as nx
from amizade import Amizade
from mensagem import Mensagem
from usuario import Usuario

class GrafoSocial:
    """
    Classe para representar e analisar um grafo social.
    """
    def __init__(self, usuarios, amizades, mensagens):
        self.grafo = nx.Graph()
        self.usuarios = {u['id']: Usuario(**u) for u in usuarios}
        self.amizades = [Amizade(**a) for a in amizades]
        self.mensagens = [Mensagem(**m) for m in mensagens]
        self.criar_grafo()

    def criar_grafo(self):
        """Constrói o grafo adicionando nós e arestas com pesos baseados em mensagens, tempo de amizade e amigos em comum."""
        for usuario in self.usuarios.values():
            self.grafo.add_node(usuario.id, nome=usuario.nome)
        
        for amizade in self.amizades:
            u1, u2 = amizade.usuario1_id, amizade.usuario2_id
            tempo_amizade = (datetime.now() - amizade.data_inicio).days
            
            # Contar mensagens trocadas
            mensagens_trocadas = sum(1 for m in self.mensagens if {m.remetente_id, m.destinatario_id} == {u1, u2})
            
            # Calcular amigos em comum
            amigos_u1 = set(self.grafo.neighbors(u1))
            amigos_u2 = set(self.grafo.neighbors(u2))
            amigos_comuns = len(amigos_u1 & amigos_u2)
            
            # Peso
            peso = mensagens_trocadas + (tempo_amizade / 365) + amigos_comuns
            self.grafo.add_edge(u1, u2, peso=peso, mensagens=mensagens_trocadas, tempo_amizade=tempo_amizade, amigos_comuns=amigos_comuns)

    def visualizar_grafo(self):
        """Gera uma visualização do grafo social com os pesos das arestas representados por espessura e cor."""
        pos = nx.spring_layout(self.grafo, seed=42)
        edges, weights = zip(*nx.get_edge_attributes(self.grafo, 'peso').items())
        
        plt.figure(figsize=(10, 10))
        nx.draw_networkx_nodes(self.grafo, pos, node_size=700, node_color='skyblue')
        nx.draw_networkx_labels(self.grafo, pos, labels=nx.get_node_attributes(self.grafo, 'nome'))
        edge_collection = nx.draw_networkx_edges(
            self.grafo, pos, edgelist=edges, width=[w / 10 for w in weights], edge_color=weights, edge_cmap=plt.cm.Blues
        )
        
        # Adicionar a barra de cores corretamente
        plt.colorbar(edge_collection, label="Peso das Arestas")
        plt.title("Grafo Social com Pesos")
        plt.show()

    def recomendar_amizades(self, usuario_id):
        """
        Sugere novas amizades para um usuário com base no número de amigos em comum.
        
        Args:
            usuario_id (int): ID do usuário para recomendação.
        
        Returns:
            list: Lista de tuplas (nome do usuário recomendado, número de amigos em comum).
        """
        amigos_diretos = set(self.grafo.neighbors(usuario_id))
        recomendacoes = []

        # Iterar sobre todos os usuários no grafo, exceto o próprio usuário
        for usuario in self.grafo.nodes:
            if usuario != usuario_id and usuario not in amigos_diretos:
                # Contar amigos em comum
                amigos_em_comum = len(amigos_diretos & set(self.grafo.neighbors(usuario)))
                
                # Se tiver pelo menos 1 amigo em comum, adicionar à lista de recomendações
                if amigos_em_comum > 0:
                    recomendacoes.append((usuario, amigos_em_comum))
        
        # Ordenar recomendações pelo número de amigos em comum em ordem decrescente
        recomendacoes.sort(key=lambda x: x[1], reverse=True)
        
        # Retornar uma lista de nomes e número de amigos em comum
        return [(self.usuarios[rec[0]].nome, rec[1]) for rec in recomendacoes]
    

    def analisar_amigos_em_comum(self, usuario_id):
        """
        Exibe a lista de amigos diretos e o número de amigos em comum entre o usuário e cada amigo.

        Args:
            usuario_id (int): ID do usuário para análise.
        """
        # Obter os amigos diretos do usuário
        amigos_diretos = list(self.grafo.neighbors(usuario_id))
        
        # Exibir amigos diretos
        print(f"Amigos diretos de {self.usuarios[usuario_id].nome}: {[self.usuarios[amigo].nome for amigo in amigos_diretos]}")
        
        # Calcular e exibir amigos em comum para cada amigo direto
        for amigo in amigos_diretos:
            # Encontrar interseção entre os amigos diretos do usuário e os amigos do amigo
            amigos_comuns = len(set(amigos_diretos) & set(self.grafo.neighbors(amigo)))
            print(f"{self.usuarios[usuario_id].nome} e {self.usuarios[amigo].nome} têm {amigos_comuns} amigos em comum.")
