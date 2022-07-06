from copy import copy
from igraph import *
from collections import deque
import random


gado = [
    {
        "id": 0,
        "vitamina": "A",
        "nome": "A00",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 1,
        "vitamina": "B",
        "nome": "A01",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 2,
        "vitamina": "C",
        "nome": "A02",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 3,
        "vitamina": "C",
        "nome": "A03",
        "nasc": "11/02/2022",
        "genero": "F",
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 4,
        "vitamina": "B",
        "nome": "A04",
        "nasc": "11/02/2022",
        "genero": "M",
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 5,
        "vitamina": "A",
        "nome": "A05",
        "nasc": "11/02/2022",
        "genero": "F",
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 6,
        "vitamina": "B",
        "nome": "A06",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 7,
        "vitamina": "A",
        "nome": "A07",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 8,
        "vitamina": "C",
        "nome": "A08",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 9,
        "vitamina": "C",
        "nome": "A09",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 10,
        "vitamina": "B",
        "nome": "A10",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 11,
        "vitamina": "A",
        "nome": "A11",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 12,
        "vitamina": "A",
        "nome": "A12",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 13,
        "vitamina": "A",
        "nome": "A13",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 14,
        "vitamina": "A",
        "nome": "A14",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 15,
        "vitamina": "A",
        "nome": "A15",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 16,
        "vitamina": "A",
        "nome": "A16",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 17,
        "vitamina": "A",
        "nome": "A17",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 18,
        "vitamina": "A",
        "nome": "A16",
        "nasc": "11/02/2022",
        'genero': 'M',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 19,
        "vitamina": "A",
        "nome": "A16",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
    {
        "id": 20,
        "vitamina": "A",
        "nome": "A16",
        "nasc": "11/02/2022",
        'genero': 'F',
        'indices': [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
    },
]

g = Graph(directed=False)


def plot_graph(grapg):
    plot(grapg,
         layout='circle',
         bbox=(1000, 1000),
         margin=50,
         vertex_label_dist=-1.8,
         vertex_shape='circle',
         vertex_size=30,
         edge_arrow_size=0.5,
         edge_label_dist=0,
         edge_curved=False)


def define_grafo(grafo, data):
    grafo.add_vertices(len(data))

    # conecta todos os vertices (grafo completo)
    indice = 0
    for v in data:
        lista = data.copy()
        lista.pop(indice)
        for j in lista:
            grafo.add_edge(v['id'], j['id'])
        indice = indice + 1

    # define os atributos de cada vertice
    for x in range(len(data)):
        grafo.vs[x]['id'] = data[x]['id']
        grafo.vs[x]['nome'] = data[x]['nome']
        grafo.vs[x]['indices'] = data[x]['indices']
        grafo.vs[x]['label'] = data[x]['nome']
        grafo.vs[x]['genero'] = data[x]['genero']
        if data[x]['genero'] == 'M':
            grafo.vs[x]['color'] = 'red'
        else:
            grafo.vs[x]['color'] = 'white'

    plot_graph(grafo)


define_grafo(g, gado)

cores = [
    {'id': 0, 'color': 'yellow'},
    {'id': 1, 'color': 'green'},
    {'id': 2, 'color': 'blue'},
    {'id': 3, 'color': 'pink'},
    {'id': 4, 'color': 'black'},
    {'id': 5, 'color': 'red'},
]


def med_indice(indices):
    soma = 0
    for x in indices:
        soma = soma + x
    media = round(soma / len(indices))
    if media >= 0 and media <= 4:
        obj = {
            'media': 'baixa',
            'color': 'blue',
            'width': media
        }
        return obj
    elif media >= 4 and media <= 6:
        obj = {
            'media': 'media',
            'color': 'green',
            'width': media
        }
        return obj
    else:
        obj = {
            'media': 'alta',
            'color': 'yellow',
            'width': media
        }
        return obj


def relaciona(xgraph):

    lista_m = []
    lista_f = []
    for x in g.vs:
        if x.attributes()['genero'] == 'M':
            lista_m.append(x)

        else:
            lista_f.append(x)
    for u in lista_m:
        media_m = med_indice(u['indices'])
        for i in lista_f:
            media_f = med_indice(i['indices'])
            if media_m['media'] == media_f['media']:
                aresta = xgraph.get_eid(u['id'], i['id'])
                xgraph.es[aresta]['color'] = media_m['color']
                print(u.attributes()['nome'],
                      media_m['media'], aresta, i.attributes()['nome'])

    plot_graph(xgraph)


relaciona(g)


def basico(xgraph):
    for x in g.es:
        x['color'] = 'white'
    lista_m = []
    lista_f = []
    for x in g.vs:
        if x.attributes()['genero'] == 'M':
            lista_m.append(x)
        else:
            lista_f.append(x)
    for u in lista_m:
        media_m = med_indice(u['indices'])
        for i in lista_f:
            media_f = med_indice(i['indices'])
            if media_m['media'] == media_f['media']:
                aresta = xgraph.get_eid(u['id'], i['id'])
                xgraph.es[aresta]['color'] = media_m['color']
                print(u.attributes()['nome'],
                      media_m['media'], aresta, i.attributes()['nome'])

    plot_graph(xgraph)


basico(g)

# v = 0
# for x in machos:
#     y = med_indice(x['indices'])

#     for i in femeas:
#         p = med_indice(i['indices'])
#         if y['media'] == p['media']:
#             # print(x['nome'], i['nome'], y['media'], p['media'])
#             # g.add_edge(x['id'], i['id'])
#             g.es[v]['color'] = p['color']
#             tamanho = (p['width'] + y['width']) / 3
#             g.es[v]['width'] = tamanho

#             v = v + 1

# plot(g,
#      layout='kk',
#      bbox=(1000, 1000),
#      margin=50,
#      vertex_label_dist=-1.8,
#      vertex_shape='circle',
#      vertex_size=30,
#      edge_label_dist=0,
#      edge_curved=False)


# indice = 0
# indice_aresta = 0
# for i in gado:
#     gado2 = gado.copy()
#     gado2.pop(indice)

#     for u in gado2:
#         if i['vitamina'] == u['vitamina']:
#             g.add_edge(i['id'], u['id'])
#             print(i['nome'], i['vitamina'], ' = ', u['nome'],
#                   u['vitamina'], '?', 'Sim')
#             for x in cores_aux:
#                 if i['vitamina'] == x['associado']:
#                     print(i['nome'], i['vitamina'],  u['nome'],
#                           u['vitamina'], x['color'])
#                     cor = x['color']

#                     g.es[indice_aresta]['color'] = cor
#                     indice_aresta = indice_aresta + 1
#         else:
#             print(i['nome'], i['vitamina'], ' = ', u['nome'],
#                   u['vitamina'], '?', 'Não')
#     if (i["genero"] == 'M'):
#         print('macho')
#         g.vs[indice]['color'] = 'red'
#     else:
#         print('femea')
#         g.vs[indice]['color'] = 'white'
#     indice = indice + 1


def Grafo(xgraph, source):
    for vertice in range(xgraph.vcount()):
        xgraph.vs[vertice]['cor'] = 'RED'
        xgraph.vs[vertice]['color'] = 'red'
        xgraph.vs[vertice]['pai'] = None
        xgraph.vs[vertice]['distancia'] = 0

    xgraph.vs[source]['cor'] = 'CINZA'
    xgraph.vs[source]['color'] = 'white'
    xgraph.vs[source]['distancia'] = 0
    xgraph.vs[source]['pai'] = None
    fila = deque()
    fila.append(xgraph.vs[source])

    while fila:
        u = fila.popleft()
        vizinhos = u.neighbors()
        for vertice in vizinhos:
            if vertice['cor'] == 'RED':
                vertice['color'] = 'gray'
                vertice['distancia'] = u.attributes()['distancia'] + 1
                print(vertice['distancia'])
                fila.append(vertice)
        u['color'] = 'black'
        u['cor'] = 'PRETO'


# Grafo(g, 6)
