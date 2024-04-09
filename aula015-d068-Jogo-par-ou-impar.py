'''Faça um programa que jogue par ou ímpar com o computador. O jogo será
interrompido quando o usuário perser, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo'''


from random import randint
v = 0
print('=-'*12)
print('JOGO DO PAR OU ÍMPAR!')
print('=-'*12)
while True:
    jogador = int(input(('Digite um valor: ')))
    computador = randint(0, 10)
    tot = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}\nTotal foi: {tot} ',  end = '')
    print('DEU PAR' if tot %2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print ('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCÊ VENCEU {v} vezes.')
