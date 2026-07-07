a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
for i in range(10):
    trm = a1 + i * r
    print(trm, end=' ')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao #formula de PA
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' -> ')
print('Acabou')
