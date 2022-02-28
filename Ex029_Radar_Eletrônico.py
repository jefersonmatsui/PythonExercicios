#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


#MULTADO! Você excedeuo limite permitido que é de 80km/km
#Você deve pagar uma multa de R${}

#Tenha um bom dia! Dirija com segurança!


velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeuo limite permitido que é de 80km/km.')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')