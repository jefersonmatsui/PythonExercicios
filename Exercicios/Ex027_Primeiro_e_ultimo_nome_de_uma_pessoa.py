#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = (str(input('Digite o seu nome completo: '))).strip().title()
print('Muito prazer em te conhecer!')
fatia = nome.split()
print('Seu primeiro nome é {}'.format(fatia[0]))
print('Seu último nome é {}'.format(fatia[-1]))

"""
n = (str(input('Digite o seu nome completo: '))).strip()
print('Muito prazer em te conhecer!')
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome(len(nome) - 1))


"""