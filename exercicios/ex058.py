a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
i = 0
while i < 10:
    trm = a1 + i * r
    print(trm, end=' ')
    i += 1
print('\n')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao
c = primeiro
while c < decimo:
    print(f'{c}', end=' -> ')
    c += razao
print('Acabou')
