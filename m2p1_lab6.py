'''
Centro Universitário Adventista de São Paulo
Campus SP

Turma       : CI73A2019
Aluno       : Gilson Nunes dos Santos Junior
RA          : 96992
Matéria     : Desenvolvimento Web
Professor   : Clodonil Honorio Trigo
Módulo      : https://github.com/clodonil/Python-Fundamentals/tree/master/modulo2/parte1/Labs/code

Data        : 10 de Maio de 2019
Descrição   : Apresenta o nome dos membros de um órgão público, a partir de sua ID, em ordem alfabética
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos os objetos
listJson = DadosAbertos()
listaMembros = set()
contador = 0

# Solicitamos que o ID seja solicitado
orgaoID = input('Digite o ID do órgão a listar os membros (ex. 5973) : ')

# Laço que armazena os dados
for comissao in  listJson.orgaos_membros(orgaoID):
    listaMembros.add(comissao['nome'])

# Ordenar elementos
listaMembros = sorted(listaMembros)

# Apresentar elementos
for nome in listaMembros :
	print("#{0} - {1}".format(contador + 1, listaMembros[contador]))
	contador = contador + 1
