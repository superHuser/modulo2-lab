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

for item in listJson.orgaos():
    id = item['id']
    nome = item['nome']
    if int(id) <= 2009 :
        print(id, nome.upper())
