from __future__ import division

# X é o numero no qual queremos a raiz quadrada
# I quantidade de interações

def calc_raizq(x, chute, i):
    if i < 1:
        raise ValueError("É necessário pelo menos uma iteração")
    if chute < 1:
        chute = 1
    if x < 0:

        return complex(0, calc_raizq(-x, chute, i))
    else:
        for n in range(i):
            chute = 1/2*(chute+x/chute)
        return chute

print(calc_raizq(9, 3, 3)) 

#Para trabalhar com numeros complexos é mais comum o uso do modulo CMATH
#https://docs.python.org/3/library/cmath.html


