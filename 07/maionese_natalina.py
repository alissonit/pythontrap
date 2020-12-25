#EXEMPLO 2
import sys

maionese = input("Insira os itens da maionese, separados por virgula: ").split(",")

print("verificando itens maionese natalina...")

if "uvas passas" in maionese:
    print("Tem uvas passas, nao quero :(")
elif "maca" in maionese:
    print("Tem maça, nao quero :(")
else:
    print("So legumes, eu quero :)")