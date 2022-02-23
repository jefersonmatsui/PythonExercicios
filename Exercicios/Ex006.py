# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
s = n ** (1/2)
print('Dobro do número {} é {}, o triplo é {} e a raiz quadrada é {:.3}'.format(n, d, t, s))

"""
Resposta
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2)))) 
"""