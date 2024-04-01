for c in range(0,6):
    print('Oi')
print('FIM')

for c in range(1,6): #a contagem será sempre um número menor, neste caso ele vai contar até 5
    print(c)
print('FIM')

for c in range(1,6, -1): #para contagem de números descrescente é só acrescentar -1
    print(c)
print('FIM')

for c in range(0,6, 2): #para contagem de números pulando 2 casas
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1): # neste caso ele vai contar até o número escolhido por causa do n+1
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1,p): # neste caso está indicando o inicio, fim e os passos entre eles
    print(c)
print('FIM')

