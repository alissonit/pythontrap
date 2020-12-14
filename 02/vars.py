#EXEMPLOS DE VARIÁVEIS

nome = 'Alisson' #STRING

idade = 27 #INT

peso = 112.00 #FLOAT

casado = True #BOLEAN

complexo = 0+3j #COMPLEX

pais, estado, cidade = 'BR', 'SP', 'SA' #MULTIPLAS ATRIBUICOES

irmaos = ['Jose', 'Maria'] #LISTA

avos = ('Francisco', 'Josefa') #CONSTANTE

#DICT
carros = {
    'SUV':'Eco Sport',
    'Hatch':'Celta',
    'Sedan':'Civic'
}

info = []

#ADICIONANDO VARS PARA LISTA INFO
info.extend([nome,idade,peso,casado,complexo,pais,estado,irmaos,avos,carros])

#LOOPING PARA PRINT DO NOME E TIPO DA VAR
for var in info:
    print(f'{var}: {type(var)}')
