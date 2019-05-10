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
Descrição   : 
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos os objetos
listJson = DadosAbertos()
deputado = listJson.deputados()
print(deputado[0])

#despesas = listJson.deputado_despesas('73437')
#for despesa in despesas:
#    print("{2}, {3}, {0}/{1}, R$ {4}".format(despesa['mes'],despesa['ano'],nome,despesa['tipoDespesa'],despesa['valorDocumento']))
