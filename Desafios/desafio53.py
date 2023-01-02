frase = str(input('Digite uma frase: ')).strip().upper() # eliminei os espaços antes e depois
palavras = frase.split() # separei cada palavra em um array
junto = ''.join(palavras) # juntei, eliminando os espaços internos
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')