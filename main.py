import json
import sys
import os
from grafoSocial import GrafoSocial

# Defina o caminho absoluto para o arquivo JSON na pasta Downloads
BASE_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "dataset_rede_social_ficticia.json")

if __name__ == "__main__":
    # Carregar os dados do JSON
    try:
        with open(BASE_PATH, 'r') as f:
            dados = json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho '{BASE_PATH}'")
        sys.exit(1)

    # Criar o grafo social com os dados
    grafo_social = GrafoSocial(dados['usuarios'], dados['amizades'], dados['mensagens'])

    # Visualizar o grafo
    grafo_social.visualizar_grafo()

    # Escolher um usuário para testes (por exemplo, Alice com id=1)
    usuario_id = 1

    # Análise de Amigos em Comum
    print("\n--- Análise de Amigos em Comum ---")
    grafo_social.analisar_amigos_em_comum(usuario_id=usuario_id)  # Exemplo com Alice (id=1)

    # Recomendação de Amizades
    print("\n--- Recomendações de Amizades ---")
    recomendacoes = grafo_social.recomendar_amizades(usuario_id=usuario_id)
    print("Recomendações de amizade para o usuário:", recomendacoes)
