# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('O aluno tirou na primeira prova a nota {:.2f}, na segunda prova tirou a nota {:.2f}, sendo assim a sua média final {:.2f}.'.format(n1, n2, m))
