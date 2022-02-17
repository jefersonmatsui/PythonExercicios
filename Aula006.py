"""Aula 6 – Tipos Primitivos e Saída de Dados

Nessa aula, vamos aprender como funcionam os tipos primitivos no Python
e as peculiaridades do int() float() bool() e str().
Além disso, veremos como fazer as primeiras
operações com a função print() do Python.

int() - número inteiro - [ 7, -4, 0, 9875]
float() - número real - [4.5, 0.076, -15.223, 7.0]
bool() - valores booleanos - [True, False]
str() - String - ['Olá', '7.5', '']

print('A soma vale', s)
print('A soma vale {}'.format(s))

"""

n1 = input('Digite um valor: ')
print(type(n1))
print()

n2 = int(input('Digite um valor: '))
print(type(n2))
print()

n3 = int(input('Digite um valor: '))
n4 = int(input('Digite outro: '))
s = n3+n4
print('A soma vale {}'.format(s))
print()
#Se não tiver o 'int' antes ele vai concatenar, isso é juntar um número com outro exemplo 5+6 = 56

n5 = int(input('Digite um valor: '))
n6 = int(input('Digite outro: '))
s = n5+n6
print('A soma entre {} e {} vale {}'.format(n5, n6, s))
print()

n7 = float(input('Digite um valor: '))
print(n7)
print()

n8 = bool(input('Digite um valor: '))
print(n8)
print()

n9 = input('Digite um valor: ')
print(n9.isnumeric())
print()

n9 = input('Digite um valor: ')
print(n9.isalpha())
print()