'''Desenvolva um progrma que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média da idade do grupo, qual é o nome do
homem mais velho e quantas mulheres tem menos de 20 anos'''



somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('===== {}ª PESSOA ====='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Gênero [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and gen in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if gen in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if gen in 'Ff' and idade < 20:
        totmulher20 +=1

mediaidade =somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velhor tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
