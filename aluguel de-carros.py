dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km Rodados?'))
pago = (dias* 60)+ (km * 0.50)
print(f' O total a pagar será de R${pago}')