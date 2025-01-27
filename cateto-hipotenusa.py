import math
co = float(input('Digite seu Cateto Oposto:'))
ca = float(input('Digite seu Cateto Abjacente:'))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')