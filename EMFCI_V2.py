import shapefile

"""
Objeto 1: shapefile reader
    Fields sf.fields cabeçalho atributos
    Records sf.record(n) atributo
    Shapes sf.shape(n) coordenadas

Objeto2: shapefile writer
    Local
    Nome
    Codificação
    Tipo


Cria campo 
fields = sf.fields

[('DeletionFlag', 'C', 1, 0), ['CODE', 'C', 254, 0], ['layer', 'C', 254, 0], ['path', 'C', 254, 0], ['Area_ha', 'N', 21, 2]]

records = sf.record(n)
>>> dicio = records.as_dict()
>>> sorted(dicio.items())
[('Area_ha', 11.2), ('CODE', '22'), ('layer', ''), ('path', '')]
>>> dicio
{'CODE': '22', 'layer': '', 'path': '', 'Area_ha': 11.2}
>>> dicio['CODE']
'22'

shapes = sf.shape(n)
>>> shapes.points 
>>> sf.shape(n).points
[(741272.1017280837, 7347142.216464439), (741042.4705364171, 7347589.7466445025), (741258.2380510662, 7347650.8308120575), (741491.3697600013, 7347292.432481371), (741272.1017280837, 7347142.216464439)]
>>>

    SÃO 3 ITENS PARA TRABALHAR, AO TRABALHAR COM O ATRIBUTO DEVEMOS SINCRONIZAR O 
VALOR DO ITEM COM O POLIGONO "sf.shape(1) sf.record(1)" 
OS CABEÇALHOS NÃO PRECISAM DE SINCRONIZAÇÃO

    PARA ALTERAR O VALOR DOS POLÍGONOS TEMOS QUE REDEFINIR O LEITOR:
"sf.shape(1) sf.record(1)" PARA "sf.shape(2) sf.record(2)"
    LEMBRE-SE QUE ALÉM DO INDEX DELE "shapes.oid"  NA NOSSA APLICAÇÃO VAMOS USAR O
"['CODE', 'C', 254, 0]" PARA SABER COM QUAL GLEBA TRABALHAR, E NO CASO DO
APLICATIVO ANTIGO TÍNHAMOS QUE COMPARAR O VALOR DO LEITOR COM O VALOR DA GLEBA DO
DICIONÁRIO. 
    UMA OPÇÃO É TER OS VALORES DAS COORDENADAS DE CADA GLEBA "shapes" EM
UMA CLASSE "class Gleba" E PUXAR O VALOR DO POLÍGONO DA LISTA/TXT DE ACORDO COM O
NÚMERO DO DICIONÁRIO QUE ESTIVERMOS TRABALHANDO, PARA DEIXAR O APP MAIS RÁPIDO.

EX: dicionario[sf.record(1)[0]] = sf.shape(1).points
    dicionario[sf.record(1)['CODE']] = sf.shape(1).points
>>> dicionario
{1: 0, 2: 0, 3: 0, '22': [(741272.1017280837, 7347142.216464439), (741042.4705364171, 7347589.7466445025), (741258.2380510662, 7347650.8308120575), (741491.3697600013, 7347292.432481371), (741272.1017280837, 7347142.216464439)]}
>>> dicionario[str(22)][1][0]
741042.4705364171

with shapefile.Writer(fr'{path}\{texto}',encoding = 'windows-1252', shapeType = 5) as w:

w.poly(dicionario[str(22)])
w.record(dicionário_valores['CODE'], areas_dict[hoje][gleba])


    ASSUMINDO-SE QUE TODO SHAPE TEM UM ATRIBUTO DE REFERÊNCIA "CODE", PODEMOS ESCREVER ELE
"""
#LEITOR
elemento = 0
e = 0
class Ponto:
    pass
"""INSIRA O NOME DA MEMORIA
INSIRA O NOME DO POLIGONO A LER
"""


class Shape:
    def __init__(self):
        self.geometria = {}
        self.cabeçalho = {}
        self.leitor_shapefile(caminho = 'C:\Program Files\Taxa fácil', nome_arquivo = 'Aguaclara_20221', geometria = self.geometria, cabeçalho = self.cabeçalho) #posição ou nome
        self.lista_tudo

    def leitor_shapefile(self, caminho, nome_arquivo, geometria, cabeçalho):
        global sf
        sf = shapefile.Reader(fr'{caminho}\{nome_arquivo}')
        self.cabeçalhos = sf.fields
        contador = 0
        while contador < len(sf):
            geometria[sf.record(contador)['CODE']] = sf.shape(contador).points
            cabeçalho[sf.shape(contador).oid] = sf.record(contador)
            contador += 1

    def lista_tudo(self):
        e = 0
        while e < len(sf):
            print(sf.record(e))
            e += 1

    def procura(self, chaves):
        self.lista_cabeçalhos = list(self.cabeçalho)
        

    def indexar(self, chaves):
        self.geometria[str(chave)]



"""
    def add_poligono(self):
        while contador < len(sf):

"""