#COMO CRIAR DICIONÁRIOS EM PYTHON (DICT) 
# CRIANDO UM DICT
d = {"Nome":"PythonTrap", "Idade":1, "Cor":"verde"}

# CRIANDO DICT USANDO BUILT-IN
d_built = dict([("Nome", "PythonTrap"), ("Idade", 1),("Cor", "verde")])

#CRIANDO UM DICT USANDO PALAVRA_CHAVE (KEYWORD)
d_keyword = dict(Nome="PythonTrap", Idade=1, Cor="Verde")

#ACESSANDO OS VALORES DO DICT
d["Nome"]

d_built["Idade"]

d_keyword["Cor"]

#ADICIONANDO UM VALOR EM UM DICT EXISTENTE

d["Cidade"] = "SP"

#REMOVENDO UM VALOR EM UM DICT EXISTENTE
del d_keyword["Cor"]

#### USANDO MÉTODOS BUILT-IN DE LISTAS
d.clear() #REMOVE TODOS OS VALORES

d_keyword.get("Nome") #PROCURA A CHAVE (KEY) DENTRO DO DICIONARIO

d_keyword.items() #RETORNA UMA LISTA DE TUPLAS CONTENDO CHAVE E VALOR (KEY-VALUES)

d_keyword.keys() #RETORNA UMA LISTA COM TODAS AS CHAVES (KEYS)

d_keyword.values() #RETORNA UMA LISTA COM TODOS OS VALORES (VALUES)

d_keyword.pop("Nome") #REMOVE A CHAVE (KEY-VALUE) DO DICIONARIO

d_keyword.popitem() #REMOVE A ULTIMA CHAVE E VALOR (KEY-VALUE) DO DICIONARIO

### ATUALIZANDO DICT COM OUTRO DICT OU KEY-VALUE
d_keyword2 = {"Lecrae":"Trap", "Number":10}

d_keyword.update(d_keyword2)

d_keyword2.update(Ano=2020)





