print('=== SALÁRIO - NOVO AUMENTO ===')
print()
sal=float(input('Digite seu salário: R$ '))
aum_sal= sal * 15/100
n_sal= sal + aum_sal
print('Seu novo salário é de R$ {}'.format(n_sal))