
#ESTRUTURA CONDICIONAL IF-ELIF-ELSE

#FUNÇÃO GERA ARVORE (vamos falor sobre elas em breve).
def get_arvore(n):
    print("Feliz Natal!")
    z = n - 1
    x = 1
    # pylint: disable=unused-variable
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x+=2
        z-=1

#NATAL 2020
from datetime import datetime

natal_data = datetime.strptime("25122020", "%d%m%Y")

try:
    #RECEBENDO VALORES
    print("Informe a data do natal em numeros:")
    data = int(input("insira o dia: "))
    mes = int(input("insira o mes: ")) 
    ano = int(input("insira o ano: "))

    dt_input = datetime.strptime(f"{data}{mes}{ano}", "%d%m%Y")
    
    #IF
    if natal_data == dt_input:
        #execução do bloco de instruções (statements)
        get_arvore(5)

    #IF - ELIF - ELSE
    if natal_data == dt_input:
        get_arvore(5)
    elif natal_data > dt_input:
        print(f"Data inferior ao dia de Natal")
    elif natal_data < dt_input:
        print(f"Data posterior ao dia de Natal")
    else:
        print("data invalida!")
except (TypeError, ValueError) as err:
    raise err
