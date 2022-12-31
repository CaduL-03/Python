prod = float(input('Qual é o preço do produto ? '))
desc = prod - (0.05 * prod)
print('O valor de ${} reais descontado a 5% é ${} reais'.format(prod,desc))