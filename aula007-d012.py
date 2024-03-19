preco = float(input('Digite o valor do produto: R$ '))
pc_tot = preco * 5/100
total_des = preco - pc_tot
print('O valor do produto com desconto é de R$ {}'.format(total_des))