# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite um valor em metros: '))
centi = metros * 100
mili = metros * 1000
print('O valor de {:.0f}m, tem {:.0f}cm e {:.0f}mm'.format(metros, centi, mili))

"""
Respostas

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {:.0f}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

"""
#Resposta 2
medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.0f}m corresponde a {:.3f}km, {:.2f}hm, {:.1f}dm, {:.0f}cm e {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))

