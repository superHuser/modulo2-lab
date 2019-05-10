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
Descrição   : Programa com otimização de execução; exibe cada ID de deputado, seu nome e sigla do partido.
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos objetos
listaDeputados = DadosAbertos()
mascara = "Id: {0}\n> Nome: {1}\n> Sigla do Partido: {2}\n"

# Percorre cada item na lista
for item in listaDeputados.deputados():
    id = item['id']
    nome = item['nome']
    # Imprime utilizando a máscara
    print(mascara.format(id, nome, item['siglaPartido']))
