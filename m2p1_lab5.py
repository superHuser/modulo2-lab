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
Descrição   : Apresenta o ID e descrição dos dez primeiros títulos do congresso.
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos objetos
listJson = DadosAbertos()

# Percorre os itens da lista
for item in listJson.orgaos():
    id = item['id']
    nome = item['nome']
    # O décimo ID é 2009, vamos imprimir até ele
    if int(id) <= 2009 :
        print(id, nome.upper())
