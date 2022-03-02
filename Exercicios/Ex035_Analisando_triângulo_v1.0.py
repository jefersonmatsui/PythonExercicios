# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

print('=-'*15)
print('ANALISADOR DE TRIÂNGULOS')
print('=-'*15)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro Segmento: '))
if a + b >= c and b + c >= a and a + c >= b:
    print('Os segmentos acima PODEM FORMAR triângulos')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triãngulo')
