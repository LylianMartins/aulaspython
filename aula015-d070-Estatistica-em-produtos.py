'''Crie um proograma que leia o nome, numero e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não.
No final mostre:

qual é o gasto da compra
quantos produtos custam mais de 1000,00
qual é o nome do produto mais barato'''

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o valor do produto? R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Valor total da compra foi de R$ {total:.2f}')
print(f'Produtos que somam mais de R$ 1000,00 = {totmil}')
print(f'Nome do produtos mais barato é o(a): {barato} que custa R$ {menor:.2f}')