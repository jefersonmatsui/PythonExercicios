# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: ' ))
if ano == 0:
    ano = date.today().year
# ano divísivel por 4, se der zero é bissexto
# e também não pode ser divisivel por 100, diferente de 0
# ou ser divisivel por 400 igual 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO É BISSEXTO'.format(ano))