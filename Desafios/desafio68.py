import random
valor = cont = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
computador = random.randint(1,10)
while True:
    jogador = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print('-'*30)
    valor = jogador + computador
    if valor % 2 == 0 and esc == 'P':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {valor} DEU PAR')
        print('-'*30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        cont += 1
    elif valor % 2 != 0 and esc == 'I':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {valor} DEU ÍMPAR')
        print('-'*30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Você venceu {cont} vezes')
        break
    
