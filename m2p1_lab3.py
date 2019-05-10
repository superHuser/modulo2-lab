'''
Centro Universitário Adventista de São Paulo
Campus SP

Turma       : CI73A2019
Aluno       : Gilson Nunes dos Santos Junior
RA          : 96992
Matéria     : Desenvolvimento Web
Professor   : Clodonil Honorio Trigo
Módulo      : https://github.com/clodonil/Python-Fundamentals/tree/master/modulo2/parte1/Labs/code

Data        : 09 de Maio de 2019
Descrição   : Apresenta o nome do canditado e seu partido, em ordem alfabética.
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos os objetos
listJson = DadosAbertos()
ldeputados = set()

# Percorremos a tabela e inserimos os itens na lista
for lista in listJson.deputados():
    nome = lista['nome']
    partido = lista['siglaPartido']
    ldeputados.add("Nome : {0}, Partido : {1}".format(nome, partido))

# Ordenamos a lista em ordem alfabética
ldeputados = sorted(ldeputados)

# Apresenta resultados
for item in ldeputados :
    print(item)
