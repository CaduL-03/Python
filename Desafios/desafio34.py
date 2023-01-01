sal = float(input('Qual é o seu salário ? '))
c10 = sal * 0.1 + sal
c15 = sal * 0.15 + sal

if sal <= 1250:
    print('Você teve um um aumento de 15%, agora recebe ${} reais'.format(c15))
else:
    print('Você teve um aumento de 10%, agora recebe ${} reais'.format(c10))