
#MODIFICANDO UMA TUPLA
tpl_values = (10, 14, 16, 20)

try:
    tpl_values[1] = 26
except (TypeError) as err:
    print(f"Error: {err}")

#ALTERANDO LISTA DENTRO DE UMA TUPLA
tpl_values = (10, 14, 16, 20, [24,26])

try:
    tpl_values[4].append(30)
    print(tpl_values)
except (TypeError) as err:
    print(f"Error: {err}")