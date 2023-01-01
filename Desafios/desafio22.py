nome = str(input('Insira seu nome: '))
nm = nome.upper()
nmi = nome.lower()
nsp = nome.replace(' ','')
npn = nome.split()

print('{}; \n {}; \n {}; \n {}; \n {}.'.format(nome, nm, nmi, len(nsp), len(npn[0])))


#frase = 'Curso em Vídeo Python'
#print(frase[::2])

#dividido = frase.split()
#print(dividido[0])
#print(dividido[2][3])

#print(frase.upper().count('o'))

#print(len(frase))

#print(frase.replace('Python', 'Android'))

#print('Curso' in frase)

#print(frase.lower().find('vídeo'))

#print(""" Generating realistic location data for users for testing or modeling simulations is a hard problem. Current approaches just create random locations inside a box, placing users in waterways or on top of buildings. """)