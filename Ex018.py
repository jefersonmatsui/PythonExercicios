# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.


'''
import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
