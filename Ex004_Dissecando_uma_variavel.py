# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(frase)))
print('Só tem espaços? {}'.format(frase.isspace()))
print('É um número? {}'.format(frase.isnumeric()))
print('É alfabético? {}'.format(frase.isalpha()))
print('É alfanumérico? {}'.format(frase.isalnum()))
print('Está em maiúsculas? {}'.format(frase.isupper()))
print('Está em minúscula? {}'.format(frase.islower()))
print('Está capitalizada? {}'.format(frase.istitle()))
