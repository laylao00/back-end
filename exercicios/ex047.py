pares = 0
for i in range(1,7):
    numero = int(input(f'Digite o {i}º número inteiro: '))
    if numero % 2 == 0:
        pares += numero
print(f'A soma dos números pares digitados é: {pares}')
