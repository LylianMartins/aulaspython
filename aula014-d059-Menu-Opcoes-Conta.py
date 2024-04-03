'''Crie um programa que leia dois valores e mostre um menu na tela:

1 - somar
 2 - multiplicar
 3 - maior
 4 - novos números
 5 sair do programa

 seu program deverá realizar a operação solicitada de cada caso'''

from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    print('=-=' * 15)
    if opção == 1:
        soma = n1 + n2
        print('A soma entre os valores {} + {} é igual a: {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é igual a: {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre os valores {} e {} o maior é: {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-='*15)
    sleep(1)
print('Fim do programa!')