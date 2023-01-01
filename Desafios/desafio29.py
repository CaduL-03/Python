vel = float(input('Qual a velocidade do carro ? '))
mul = (vel - 80) * 7

if vel > 80:
    print('Você foi multado! Valor de ${} reais.'.format(mul))
else:
    print('Você é um motorista responsável!')
