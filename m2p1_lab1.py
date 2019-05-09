
'''
Centro Universitário Adventista de São Paulo
Campus SP

Turma       : CI73A2019
Aluno       : Gilson Nunes dos Santos Junior
RA          : 96992
Matéria     : Desenvolvimento Web
Professor   : Clodonil Honorio Trigo
Módulo      : https://github.com/clodonil/Python-Fundamentals/tree/master/modulo2/parte1/Labs/code

Data        : 08 de Maio de 2019
Descrição   : Apresenta o nome e partido dos deputados encontrados, o total de deputados e partidos.
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Declaramos objetos
listaDeputados = DadosAbertos()
relacaoDeputados = []
listaPartidos = set()

# Loop para apresentar os dados
for item in listaDeputados.deputados() :
	print(item['nome'], 'do', item['siglaPartido'])
	# Listamos unicamente os partidos que obtivermos
	listaPartidos.add(item['siglaPartido'])

# Apresentamos os totais
print('\n--------------------------------------------\n')
print('Numero de deputados :', len(listaDeputados.deputados()), ', de ', len(listaPartidos), 'partidos.\n')