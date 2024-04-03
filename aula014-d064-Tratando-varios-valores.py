'''Crie um program que leia varios numeros inteiros pelo teclado.
O programa só vao parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma
entre eles (desconsiderando o flag)'''

num = 0
cont = 0
soma = 0
num = int(input('Digite um número ou [999] para parar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número ou [999] para parar: '))
print('Você digitou {} números e a soma entre eles foi: {} '.format(cont, soma))