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
Descrição   : Apresenta as depesas totais de um(a) deputado(a) pela busca de seu ID
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos os objetos, em seguida pedimos qual ID buscar
listJson = DadosAbertos()
deputado = listJson.deputados()
deputadoID = input('Digite um ID de deputado (ex. 204521) : ')
despesas = listJson.deputado_despesas(deputadoID)

# Precisamos mostrar de quem são as depesas
for linha in deputado :
	if str(linha['id']) == str(deputadoID) :
		print("\nID {0}, deputado(a) {1} : ".format(deputadoID, linha['nome']))

# Instaciamos as variáveis
criterio1 = "MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE PARLAMENTAR"
criterio2 = "LOCOMOÇÃO, ALIMENTAÇÃO E  HOSPEDAGEM"
criterio3 = "COMBUSTÍVEIS E LUBRIFICANTES."
criterio4 = "CONSULTORIAS, PESQUISAS E TRABALHOS TÉCNICOS."
criterio5 = "AQUISIÇÃO DE MATERIAL DE ESCRITÓRIO."
criterio6 = "AQUISIÇÃO OU LOC. DE SOFTWARE; SERV. POSTAIS; ASS."
criterio7 = "OUTROS"
gasto1 = 0
gasto2 = 0
gasto3 = 0
gasto4 = 0
gasto5 = 0
gasto6 = 0
gasto7 = 0
contador = 0

# Para cada descrição, atribuímos uma soma de valores
for despesa in despesas :
   if despesa['tipoDespesa'] == criterio1 :
       gasto1 = gasto1 + despesa['valorDocumento']
   elif despesa['tipoDespesa'] == criterio2 :
       gasto2 = gasto2 + despesa['valorDocumento']
   elif despesa['tipoDespesa'] == criterio3 :
       gasto3 = gasto3 + despesa['valorDocumento']
   elif despesa['tipoDespesa'] == criterio4 :
       gasto4 = gasto4 + despesa['valorDocumento']
   elif despesa['tipoDespesa'] == criterio5 :
       gasto5 = gasto5 + despesa['valorDocumento']
   elif despesa['tipoDespesa'] == criterio6 :
       gasto6 = gasto6 + despesa['valorDocumento']
   else :
       gasto7 = gasto7 + despesa['valorDocumento']

# Para facilitar a impressão, juntamos os dados
listaDespesas = [criterio1, criterio2, criterio3, criterio4, criterio5, criterio6, criterio7]
listaValores = [gasto1, gasto2, gasto3, gasto4, gasto5, gasto6, gasto7]

# Como temos sete itens nas listas, vamos imprimir as sete descrições e seus totais
while contador < 7 :
	print("  Total de gastos com {0} = R$ {1:.2f}".format(listaDespesas[contador], listaValores[contador]))
	contador = contador + 1
