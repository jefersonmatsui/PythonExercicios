#Faça um programa que leia um número inteiro e mostre na tela oseu sucessor e seu antecessor

n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('O número {}, tem como seu sucessor o número {} e o antecessor {}'.format(n, s, a))

"""
Resposta
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
"""