'''Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela:
o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais'''

n1 = int(input('==== COMPARANDO NÚMEROS ====\nDigite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número {} é maior que segundo, {}'.format(n1, n2))
elif n2 > n1:
    print ('O segundo número {} é maior que o primeiro, {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais')
