val = float(input('Qual é a distância da sua viagem ? '))
p1 = val * 0.50
p2 = val * 0.45

if val <= 200:
    print('Esse é o preço da sua passagem: ${} reais.'.format(p1))
else:
    print('Sua viagem excede os 200Km, o valor da sua passagem é de ${} reais.'.format(p2))