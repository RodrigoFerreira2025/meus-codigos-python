print('-='*20)
print('Analisador de  Triangulos')
print('-='*20)
r1 =  float(input('Primeiro Segmento'))
r2 = float(input('Segundo Segmento'))
r3 = float(input('Terceiro Segmento'))
if r1 < r2 + r3 and r2 < r1 < r3  and r3 < r1 + r2:
    print('Os Segmentos Acima pode Formar Triangulos')

else:
    print('Os Segmentos Acima nao pode Formar Triangulos:')