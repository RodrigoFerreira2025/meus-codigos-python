import random
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno:'))
n4 = str(input('Quatro Aluno:'))
n5 = str(input('Quinto Aluno:'))
lista = [n1,n2,n3,n4,n5]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')