while True:
    print('-'*50)
    tabuada = int(input('Quer ver a tabuada de qual valor ? '))
    if tabuada < 0:
        break
    for x in range(1,11):
        print(f'{tabuada} x {x} = {tabuada*x}')
