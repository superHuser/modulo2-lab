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
Descrição   : 
'''

# Importamos a biblioteca
from  lib.scrapy_dadosAbertos import DadosAbertos

# Instanciamos os objetos
listJson = DadosAbertos()
deputado = listJson.deputados()
despesas = listJson.deputado_despesas('73437')
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
listaDespesas = [criterio1, criterio2, criterio3, criterio4, criterio5, criterio6, criterio7]
listaValores = [gasto1, gasto2, gasto3, gasto4, gasto5, gasto6, gasto7]

for despesa in despesas :
   if despesa['tipoDespesa'] == crietrio1 :
       gasto1 = gasto1 + float(despesa['valorDocumento'])
   elif :
       if despesa['tipoDespesa'] == crietrio2 :
           gasto2 = gasto2 + float(despesa['valorDocumento'])
       elif :
           if despesa['tipoDespesa'] == crietrio1 :
               gasto3 = gasto3 + float(despesa['valorDocumento'])
           elif :
                if despesa['tipoDespesa'] == crietrio1 :
                    gasto4 = gasto4 + float(despesa['valordDocumento'])
                elif :
                    if despesa['tipoDespesa'] == crietrio1 :
                       gasto5 = gasto5 + float(despesa['valordDocumento'])
                    elif :
                        if despesa['tipoDespesa'] == crietrio1 :
                           gasto6 = gasto6 + float(despesa['valordDocumento'])
                        else :
                           gasto7 = gasto7 + float(despesa['valordDocumento'])
   
#print("{2}, {0}/{1}, R$ {3}".format(despesa['mes'],despesa['ano'],despesa['tipoDespesa'],despesa['valorDocumento']))
print("Total de gastos com {0} = R$ {1}")

#print(despesas)
