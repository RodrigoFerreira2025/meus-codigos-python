from random import shuffle
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno:'))
n4 = str(input('Quatro Aluno:'))
n5 = str(input('Quinto aluno:'))
lista  = [n1,n2,n3,n4,n5]
shuffle(lista)
print('A ordem de Apresentação sera:')
print(lista)