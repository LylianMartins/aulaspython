'''Crie um programa que leia a idade de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar.
No final mostrar
quantas pessoas tem mais de 18 anos
quantos homens foram cadastrados
quantas mulheres com menos de 20 anos'''

tot18 = totH = totF =  0
while True:
        print('-' * 20)
        print('CADASTRE UMA PESSOA')
        print('-' * 20)
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
                sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
                print('-' * 20)
        if idade >= 18:
                tot18 += 1
        if sexo == 'M':
                totH += 1
        if sexo == 'F' and idade <= 20:
                totF += 1

        resp = ' '
        while resp not in 'SN':
                resp = str(input('Quer continuar? S/N] ')).strip().upper()[0]
        if resp == 'N':
                break
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'Total de pessoas do gênero masculino {totH}')
print(f'Total de pessoas do gênero feminino com menos de 20 anos {totF}')
print('===== FIM DO PROGRAMA =====')
