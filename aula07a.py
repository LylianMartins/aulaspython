nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:10}!'.format(nome)) #nome com espaço
print('Prazer em te conhecer, {:>20}!'.format(nome)) # alinhamento a direita
print('Prazer em te conhecer, {:<20}!'.format(nome)) #alinhamento a esquerda
print('Prazer em te conhecer, {:^20}!'.format(nome))#alinhamento centralizado
print('Prazer em te conhecer, {:=^20}!'.format(nome)) # alinhamento centralizado com simbolo
print() # para dar espaço
print()

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s,m,d)) # casas decimais {:.3f} / \n (quebra linha)
print('Divisão inteira {} e potência {}'.format(di,e))