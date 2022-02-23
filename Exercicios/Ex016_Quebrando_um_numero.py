# Crie um programa que leia um número Real qualquer pelo teclado
# mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127, o número 6.127 tem a parte inteira 6


import math
num = float(input('Digite um valor: '))
val1 = math.trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, val1))

from math import trunc
num = float(input('Digite um valor: '))
val1 = trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, val1))


num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

