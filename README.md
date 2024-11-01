# recomendador_amizades
Com base em um conjunto de dados de uma rede social fictícia, crie e analise um grafo baseado em dados dos usuários e suas relações de amizade, visando prover recomendações de amizades.

Parte 1 — Criação do Grafo
Carregue o dataset JSON em seu ambiente Python.
Crie o grafo com os dados (usando a biblioteca NetworkX).
Calcule pesos para as arestas baseados em um ou mais dos seguintes fatores:
Quantidade de Mensagens: Número de mensagens trocadas entre os dois usuários.
Tempo de Amizade: Duração da amizade.
Amigos em Comum: Número de usuários (ou outros indicadores) de amigos de ambos.
Parte 2 — Visualização do Grafo
Gere uma visualização do grafo.
Use atributos visuais (como espessura ou cor das arestas) para representar os pesos.
Parte 3 — Análise e Sugestão de Amizades
Análise de Amigos em Comum. Dado um determinado usuário, identifique (pelo menos):
Lista de amigos diretos.
Número de amigos em comum com cada um de seus amigos.
Recomendação de Amizades. Sugira amizades para um usuário (pelo menos) com base em:
Amigos em Comum: Usuários que não são amigos diretos, mas têm amigos em comum.
Afinidade: Potencial afinidade entre usuários com base em informações disponíveis no dataset.
