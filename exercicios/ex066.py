totms18 = tothom = totmulheresmn20 = 0
while True:
    print('-'*30)
    print(' CADASTRE UMA PESSOA  ')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = input('Sexo: [M/F]').strip().upper()[0]
    if idade > 18:
        totms18 += 1
    if sexo == 'M':
        tothom += 1
    if sexo == 'F' and idade < 20:
        totmulheresmn20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]').strip().upper()[0]
    if resposta == 'N':
        break
print('\n'+'='*30)
print('     FIM DO PROGRAMA     ')
print('=' * 30)
print(f'Total de pessoas maiores de idade: {totms18}')
print(f'Total de homens: {tothom}')
print(f'Total de mulheres com menos de 20 anos: {totmulheresmn20}')
