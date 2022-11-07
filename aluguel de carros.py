dias = int(input('Quantos dias alugados?>\n>>>'))
kmRod = int(input('Quantos Km rodados?>\n>>>'))

valorPorDia = 60
valorPorKm  = 0.15
total = (dias*valorPorDia)+(kmRod*valorPorKm)

print(f'O total a pagar é R${total}')