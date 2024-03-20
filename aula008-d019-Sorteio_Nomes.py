'''Um professor quer sortear um dos seis quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo a tela o nome do sorteado'''


print()
print('==== SORTEIO PARA APAGAR O QUADRO ====')
print()
from random import choice
n1 = str(input(' Digite o nome do aluno 1: '))
n2 = str(input(' Digite o nome do aluno 2: '))
n3 = str(input(' Digite o nome do aluno 3: '))
n4 = str(input(' Digite o nome do aluno 4: '))

lista = (n1, n2, n3, n4)
sorteio = choice(lista)
print()
print ('O aluno sorteado foi: ', sorteio)

'''print()
print('==== SORTEIO PARA APAGAR O QUADRO ====')
print()
import random
n1 = str(input(' Digite o nome do aluno 1: '))
n2 = str(input(' Digite o nome do aluno 2: '))
n3 = str(input(' Digite o nome do aluno 3: '))
n4 = str(input(' Digite o nome do aluno 4: '))

lista = (n1, n2, n3, n4)
sorteio = random.choice(lista)
print()
print ('O aluno sorteado foi: ', sorteio)'''