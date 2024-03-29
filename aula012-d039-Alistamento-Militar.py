'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a dua idade:
se ela vai se aliastar ao serviço militar;
se é a hora de se alistar
se já passou do tempo de alistamento

mostrar o tempo que falta ou passou do prazo'''

from datetime import date
atual = date.today().year
print('\33>>>\33[m'*12)
print('          \33[32mALISTAMENTO MILITAR 2024\33[m')
print('\33>>>\33[m'*12)
print('  \33[7mConfira aqui se você deve se alistar esse ano\33[m')
sex = str(input('''Selecione:
[ 1 ] Sou Homem
[ 2 ] Sou Mulher'''))
opção = int(input('Escolha uma opção: '))
if opção == 2:
    print('VOCÊ NÃO PRECISA FAZER ALISTAMENTO MILITAR OBRIGATÓRIO')
    exit()
nasc = int(input('Digite ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
