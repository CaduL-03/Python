dias = float(input('Por quantos dias ele foi alugado ? '))
km = float(input('Quantos Km percorreu ? '))
pd = dias * 60
pkm = km * 0.15
result = pd + pkm
print('O valor a pagar é de ${}'.format(result))