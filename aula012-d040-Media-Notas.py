'''Crie um programa que leia dias notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a sua média:
- Média baixa de 5.0 - REPROVADO
- Média entre 5.0 e 6.9 - RECUPERAÇÃO
- Média 7.0 ou superior - APROVADO'''

print('\33[7m#### ESCOLA REINO ENCANTADO ####\33[m')
print('       Sistema de Média')
print()
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('PARABENS VOCÊ ESTÁ APROVADO. MÉDIA: ', media)
elif media > 5.0 <= 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO. MÉDIA: ', media)
else:
    print('VOCÊ FOI REPROVADO. MÉDIA: ', media)