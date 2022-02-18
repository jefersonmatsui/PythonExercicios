# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade e tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual é a largura da parede em metros: '))
altura = float(input('Qual é a altura da parede em metros: '))
area = largura * altura
pintura = area / 2
print('A parede tem a área de {:.2f}m² e são necessários {:.2f} litros de tinta para pintá-la'.format(area, pintura))


"""
larg = float(input('Qual é a largura da parede em metros: '))
alt = float(input('Qual é a altura da parede em metros: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))

"""