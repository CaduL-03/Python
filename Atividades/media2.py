valor = int(input())
total = valor
ced = 100
totalced = 0

fced = f'{ced:_.2f}'
fced = fced.replace('.',',').replace('_','.')

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced >= 0:
            print(f'{totalced} nota(s) de de R$ {fced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0
        if total == 0:
            break
