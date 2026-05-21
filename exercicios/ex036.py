casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento?'))
prestacao = casa/(financiamento*12)
if prestacao <=salario*0.3:
    print('Para pagar uma casa de {} em {} anos a prestação será de R${:.2f} é sufiiente. Empréstimo aprovado'.format(casa,financiamento,prestacao))
elif prestacao > salario*0.3:
    print('Para pagar uma casa de {} em {} anos a prestação será de R${:.2f} é muito pouco. Empréstimo negado.'.format(casa,financiamento,prestacao))
