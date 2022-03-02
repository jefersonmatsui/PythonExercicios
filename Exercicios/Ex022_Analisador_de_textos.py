#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

from time import sleep
nome = input('Digite seu nome completo: ').strip()
sleep(1)
print('Analisando seu nome...')
sleep(3)
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
sleep(1)
print('Seu nome em minúsculas é {}'.format(nome.lower()))
sleep(1)
test = nome.replace(' ','')
print('Seu nome tem ao todo {} letras'.format(len(test)))
sleep(1)
lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0])))
sleep(1)




nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0])))




