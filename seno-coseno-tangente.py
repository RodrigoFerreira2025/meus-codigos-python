import math
angulo = float(input('Digite o angulo que voce deseja:'))
seno = math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
cosseno= math.cos(math.radians(angulo))
print(f'O Angulo de {angulo} tem O COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o TANGENTE de {tangente:.2f}')