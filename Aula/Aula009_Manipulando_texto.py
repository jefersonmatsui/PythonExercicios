
#Nessa aula, vamos aprender operações com String no Python.
#As principais operações que vamos aprender são o Fatiamento de String,
#Análise com len(), count(), find(), transformações com replace(), upper(), lower(),
#capitalize(), title(), strip(), junção com join().



#frase:
#C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# Toda a String começa no número 0
# No Python há diferenças entre as letras maiúsculas e minúsculas

frase = 'Curso em Video Python'

#FATIAMENTO

#frase[9]
#- Somente o caractere 9 referente a letra "V", que em termos normais onde começa a contagem do 1, seria o 10 caractere
#- número do indice dentro da string
print(frase[9])

#frase[9:13]
#- Seleciona tudo q estiver entre o 9 e 12, o 13 não vai entrar dentro da lista
#- Ex. Vide
#- Inicio começa certo, mas sempre é um a menos do final, vai até o numero 13, mas não seleciona
print(frase[9:13])

#frase[9:21]
#- Seleciona 'Video Python'
#- Existe outra maneira melhor de fatiamento, mas funciona
print(frase[9:21])

#frase[9:21:2]
#- [começa:termina:pula]
#- Ex. VdoPto
print(frase[9:21:2])

#frase[:5]
#- Omitindo onde começa, automaticamente começa a contar do '0'(zero)
#- Ex. Curso
print(frase[:5])

#frase[15:]
#- Indica o inicio, mas omite o final da frase
#- Ex: Python
print(frase[15:])

#frase[9::3]
#- Começa no 9, vai até o final, pula de 3 em 3
#- Ex: VePh
print(frase[9::3])


#ANÁLISE

#len(frase)
#- lenght comprimento
#- qual comprimento da frase
#- Ex: o len de frase seria 21 caracteres
print(len(frase))

#frase.count('o')
#- Contar quantaas vezes aparece a letra 'o' minúsculo, se tiver 'O' maiúsculo não seria contado
#- Ex: 3
print(frase.count('o'))
print(frase.upper().count('o'))

#frase.count('o', 0, 13)
#- Contagem com fatiamento
#- (o que eu quero, quando começar, onde terminar)
#- Lembrando que nesse caso o 13 não é contabilizado
#- Ex: 1
print(frase.count('o', 0, 13))

#frase.find('deo')
#- onde vai encontrar o que foi pedido
#- Ex: 11
print(frase.find('deo'))

#frase.find('Android')
#- Quando não encontra ou nao existir o que foi pedido, vai retornar o valor -1
#- Ex: -1
print(frase.find('Android'))

#'Curso' in frase
#- Existe a palavara em(in) frase
#- Ex: True
print('Curso' in frase)

#TRANSFORMAÇÃO

#frase.replace('Python', 'Android')
#- Troca / reposicionar / substituir a palavra
#- Ex: Curso em Video Android
print(frase.replace('Python', 'Android'))

#frase.upper()
#- Mantém o que estiver em maiúsculo e o que tiver em minúsculo troca por maiúsculo
#- Ex: CURSO EM VIDEO PYTHON
print(frase.upper())

#frase.lower()
#- ao contrário do upper
#- Ex: curso em video python
print(frase.lower())

#frase.capitalize()
#- Só a primeira letra será me maiúsculo e o resto vai ficar minúsculo
#- Ex: Curso em video python
print(frase.capitalize())

#frase.title()
#- vai calcular quantas palavras tem atraves da quebra de espaços, e toas as palavras vão receber a primeira letra maiúsculo
#- Ex: Curso Em Video Python
print(frase.title())



#NOVA FRASE EXEMPLO

#         A  p  r  e  n  d  a       P   y   t   h   o   n
#0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18
frase2 = '   Aprenda Python  '


#frase.strip()
#- Remove os espaços inúteis do começo e do final
#- Ex:
#A  p  r  e  n  d  a     P  y   t   h   o   n
#0  1  2  3  4  5  6  7  8  9  10  11  12  13
print(frase2.strip())

#frase.rstrip()
#- Remove somente os espaços inúteis lado direito/ final da frase
#- Ex:
#         A  p  r  e  n  d  a       P   y   t   h   o   n
#0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16
print(frase2.rstrip())

#frase.lstrip()
#- Remove somente os espaços inúteis lado esquerdo/ inicio da frase
#- Ex:
#A  p  r  e  n  d  a     P  y   t   h   o   n
#0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
print(frase2.lstrip())

#DIVISÃO

#frase.split()
#- onde tiver espaço vai ser criado uma divisão
#- vai dividir em uma lista cada palavra vai ser dividido pelo fatiador
#Ex:
#C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
#0 1 2 3 4   0 1   0  1  2  3  4     0  1  2  3  4  5
print(frase.split())

#JUNÇÂO

#'-'.join(frase)
#C u r s o - e m - V  i  d  e  o  -  P  y  t  h  o  n
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
print('-'.join(frase))


s = 'prova de python'
print(len(s))