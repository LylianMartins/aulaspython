print('GERADOR DE TABUADA')
print()

tabuada=int(input('Tabuada de numero: '))
for count in range(10):
    print('%d x %d = %d' % (tabuada, count+1, tabuada*(count+1)))