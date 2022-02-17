"""Nessa aula, vamos aprender quais são os operadores aritméticos do Python
e também sua ordem de precedência dentro de expressões matemáticas.
Veja como funcionam os operadores de adição, subtração, multiplicação, divisão,
exponenciação e quociente na linguagem Python.

= atribuição de recebe
== igual
+ == Soma
- == Subtração
* == Multiplicação
/ == Divisão
** == Potência
// == Divisão Inteira
% == Resto da Divisão

Ordem de precedência

1 - ( ) Parentêses
2 - ** Potência
3 - *, /, //, %
4 - +, -
"""
"""
#Poder do Print
nome = str(input('Qual é seu nome? '))
print('Prazer em te conhecer {}!'.format(nome))

# Aparecer me 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome))

# Aparecer me 20 caracteres com alinhamento à direita
print('Prazer em te conhecer {:>20}!'.format(nome))

# Aparecer me 20 caracteres com alinhamento à esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))

# Aparecer me 20 caracteres com alinhamento no centro
print('Prazer em te conhecer {:^20}!'.format(nome))

# Aparecer me 20 caracteres com alinhamento no centro e com desenho
print('Prazer em te conhecer {:=^20}!'.format(nome))
"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#{:.3f] com três casas flutuantes
print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))
print()
# para não quebrar a linha coloca um end=''
print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
print()
# Quebrar a linha \n quer dizer nova linha
print('A soma vale {},\n o produto é {} e a\n divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))