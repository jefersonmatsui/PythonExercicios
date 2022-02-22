"""
Nessa aula, vamos aprender como utilizar módulos em Python utilizando
os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários recursos
adicionais nos seus programas utilizando módulos built-in e
módulos externos, oferecidos no Pypi.


import math
from math import sqrt

"""
"""
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
#math.ceil arredonda para cima
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#math.floor arredonda para baixo
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))


from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))


from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

"""
# Todos tipos de números
import random
num = random.random()
print(num)

# Todos tipos de números inteiros
import random
num = random.randint(1, 10)
print(num)

# PyPI - the Python Package Index
# lâmpada vermelha package
import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))


