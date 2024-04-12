'''crie uma tupla prenchida com 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na oredem de colocação, depois mostre
os primeiros 5 times
os ulltimos 4 colocados
times em oredem alfabética
em que posição está o time da Chapecoense'''

times = ('Cortinthians', 'Palmeiras', 'Santos','Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-Go')
print('-='*10)
for t in times:
    print(t)
print('-='*10)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*10)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*10)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
