'''Elabore um program que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
a vista 10%
a vista no cartão 5%
2x no cartão - preço normal
3x ou mais no cartão - 20% de juros'''

print('{:=^20}'.format(' LOJA CABANA '))
preço = float(input('Digite o valor do produto: R$ '))
print()
opção = int(input('ESCOLHA A FORMA DE PAGAMENTO:\n[ 1 ]- PARA DINHEIRO\n[ 2 ] - Á VISTA NO CARTÃO\n[ 3 ] - 2x PARCELADO EM 2X\n[ 4 ] - PARCELADO EM 3X ou mais\nDigite a forma escolhida:  '))
print()
if opção == 1:
    total = preço - (preço * 10 /100)
    print('Você teve um desconto de 10%\nO valor a pagar R$ {:.2f}'.format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total /2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço *20 /100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcela em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
print('Sua compra de R$ {:.2f} vai custar no total R$ {:.2f}'.format(preço, total))

print()
print('Obrigada pelas compras! Volte Sempre!')