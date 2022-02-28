#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('=-'*28)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-'*28)
numero = int(input('Em que número eu pensei? '))
adiv = randint(0, 5)
sleep(1)
print("PROCESSANDO...")
sleep(3)
if numero == adiv:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(adiv, numero))
