import random

computador = random.randint(0, 10)

palpites = 0
jogador = 11

while jogador != computador:
    jogador = int(input('Adivinhe um número de 0 a 10: '))
    print('Tente novamente!')
    palpites += 1
if jogador == computador:
    print('Você acertou em {} palpite(s)!! O número que pensei era {}'.format(palpites, computador))

    
