#Escreva um programa para aprovar um empréstimo bancário para compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode ultrapassar 30% do salário ou então
#o emprestimo será negado.

print('=-=-'*10)
print('      \33[41mPROGRAMA CASA MINHA CASA\33[m')
print('=-=-'*10)
print('\33[31mSeu empréstimo fácil, rápido e seguro\33[m')
print()
nome = (str(input('Qual o seu nome: ')))
imovel =(float(input('Qual o valor do imóvel que deseja financiar, {}: R$ '.format((nome)))))
xprest = (int(input('Em quantas prestações, deseja financiar? ')))
sal = float(input('Qual o valor do seu salário atual: R$ '))
vlprest = imovel / (xprest * 12)
cppg = sal * 30 / 100
if vlprest <= cppg:
    print('\33[32mPARABÉNS!\33[m {}, seu empréstimo foi aprovado! sua parcela será de \33[42mR$ {:.2f}\33[m'.format(nome, vlprest))
else:
    print('\33[31mSEU EMPRÉSTIMO NÃO FOI APROVADO\33[m')
