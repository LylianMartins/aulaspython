'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunose mostre a ordem sorteada'''


print('==== SORTEIO APRESENTAÇÃO DE TRABALHO ====')
print()
import random
a1 = str(input(' Digite o nome do aluno 1: '))
a2 = str(input(' Digite o nome do aluno 2: '))
a3 = str(input(' Digite o nome do aluno 3: '))
a4 = str(input(' Digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista) #suffle significa embaralhar
print()
print('OS SORTEADOS POR ORDEM FORAM: ')
print()
print(lista)


'''print('==== SORTEIO APRESENTAÇÃO DE TRABALHO ====')
print()
from random import shuffle
a1 = str(input(' Digite o nome do aluno 1: '))
a2 = str(input(' Digite o nome do aluno 2: '))
a3 = str(input(' Digite o nome do aluno 3: '))
a4 = str(input(' Digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista) #suffle significa embaralhar
print()
print('OS SORTEADOS POR ORDEM FORAM: ')
print()
print(lista)'''