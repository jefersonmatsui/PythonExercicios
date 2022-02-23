# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual é o preço do produto: R$'))
desconto = preco - (preco * (5/100))
print('O produto custa R${:.2f}, mas na liquidação com 5% de desconto o produto vai sair por R${:.2f}'.format(preco, desconto))

"""
preco = float(input('Qual é o preço do produto: R$'))
novo = preco - (preco * 5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))
"""