nas = int(input('Qual o ano do seu nascimento: '))
alis = 2023 - nas
fal = alis - 18

if alis > 18:
    print('Já passou do prazo de Alistamento.')
    print('Já passou {} anos do seu alistamento'.format(fal))
elif alis < 18:
    print('Terá que se alistar futuramente.')
    print('Falta {} anos até o seu alistamento'.format(abs(fal)))
else:
    print('Está na hora de se alistar!')
