#COMO CRIAR LISTAS EM PYTHON
#           Item 0        Item 1      Item 2
movies = ["Iron man", "Spider man", "Super Man"]

#ACESSANDO OS DADOS DA LISTA USANDO A NOTAÇÃO COLCHETES

print(movies[0]) #output -> Iron nan

#CALCULANDO ITENS DE DADOS NA LISTA

print(len(movies)) #output -> 3

#ADICIONANDO DADOS NA LISTA

movies.append("Wonder Woman")

#INSERINDO ANTES DE UM ITEM ESPECÍFICO
#O ZERO REPRESENTA O ITEM 

movies.insert(0, "Black Panther")

#REMOVENDO DADOS DA LISTA

movies.pop() #O MÉTODO POP REMOVO O ÚLTIMO DADO DA LISTA

movies.remove("Iron man") #REMOVE UM DADO ESPECIFÍCO

#ITERANDO LISTA MOVIES (VAMOS FALAR EM BREVE SOBRE ITERAÇÃO)

for movie in movies:
    print(movie)

#DICA PLUS :) PRINT LIST COMPREHENSION - (VAMOS FALAR EM BREVE SOBRE COMPREHENSION

print([movie for movie in movies])











