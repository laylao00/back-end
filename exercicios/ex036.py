valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

print(f'\nPara pagar uma casa de R$ {valor_casa:.2f} em {anos} anos,', end=' ')
print(f'a prestação será de R$ {prestacao:.2f}.')

if prestacao <= limite:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

#----------------------------------------------------

valorcasa = float(input('Qual o valor da casa em R$?'))
salario = float(input('Qual o seu salário em R$?'))
anos
