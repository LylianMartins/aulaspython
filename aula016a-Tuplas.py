# Aula de Tuplas
# Tuplas são imutáveis
# variavel compposta = (tuplas) [listas] {dicionário}

# exemplo

lanche = ('Hamburguer', 'Suco', ' Pizza', 'Batata Frita')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

#ou

'''lanche = ('Hamburguer', 'Suco', ' Pizza', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# ou mostrando a posição

lanche = ('Hamburguer', 'Suco', ' Pizza', 'Batata Frita')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# outra opção com a posição

lanche = ('Hamburguer', 'Suco', ' Pizza', 'Batata Frita')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''