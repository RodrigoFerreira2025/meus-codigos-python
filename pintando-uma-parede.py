larg = float(input("Largura da Parede:"))
alt = float(input("Altura da Parede:"))
área = larg*alt
tinta = área/ 2
print(f'\033[32;40m Sua parede tem a dimensão de {larg}x{alt},e sua area é de {área}\n')
print(f'\033[31;40m Para pintar sua parede,voce precisa de   {tinta}l\n')