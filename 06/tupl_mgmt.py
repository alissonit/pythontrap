# USANDO TUPLAS (TUPLES)
#EXEMPLO DE TUPLAS
tpl = tuple()

tpl2 = "AIR", "SKY", 2020

gru_coordinates = (-23.4322, -46.4692)

print(type(gru_coordinates))

#LISTA DE TUPLAS
air_comp = [("Azul", 8), ('GOL', 5), ("AA", 9), ("Qatar", 10)]

for comp in sorted(air_comp):
    air_name, score = comp
    print(f"comp: {air_name} score: {score}")

#DESEMPACOTAMENTOS DE TUPLAS
air_comp = [("Azul", 8), ('GOL', 5), ("AA", 9), ("Qatar", 10)]

for comp, _ in air_comp:
    print(f"comp: {comp}")

r_tpl = divmod(10, 3)

tpl = (10, 3)

r_tpl = divmod(*tpl) #USANDO ARGS COMO PARAMETRO

#capturando itens restantes
comp = ("Azul", "AA", "GOL", "Qatar", "LATAM")

air_comp1, air_comp2, *rest = comp




