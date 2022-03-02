# vamos aprender como utilizar os códigos de escape sequence ANSI
# para configurar cores para os seus programas em Python.
# Veja como utilizar o código \033[m com todas as suas principais possibilidades.

'''
ANSI
ESCAPE SEQUENCE

Cor
\033[m
    style back
\033[0;33;44m
      text

STYLE
0 == none
1 == Bold
4 == Underline
7 == Negative

Color
30 == White
31 == red
32 == green
33 == yellow
34 == blue
35 == magenta
36 == Cyan
37 == gray

Background
40 == White
41 == red
42 == green
43 == yellow
44 == blue
45 == magenta
46 == Cyan
47 == gray

'''
#Normal
print('Hello World!')
#Letra vermelha
print('\033[31mHello World!')
#Letra vermelha e fundo amarelo
print('\033[31;43mHello World!')
#Letra vermelha, fundo amarelo e negrito
print('\033[31;43;1mHello World!')
#Letra vermelha, fundo amarelo e negrito elinar a barra até o final
print('\033[31;43;1mHello World!\033[m')
#Letra branca, sublinhado fundo magenta
print('\033[4;30;45;1mHello World!\033[m')

