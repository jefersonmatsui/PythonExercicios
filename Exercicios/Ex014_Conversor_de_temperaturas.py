#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe uma temperatura em °C: '))
f = c * 1.8 + 32
print('A temperatura de {}°C corresponde a {:.1f}°F'.format(c, f))

"""
c = float(input('Informe uma temperatura em °C: '))
f = 9 * c /5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))


"""
