dias = int(input('Por quantos dias, o carro foi usado?'))
km = float(input('Quantos km foram rodados?'))
diaria = dias*60
percurso = km*0,15
custo = diaria+percurso 
print('O total a pagar é de R${:.2f}'.format(custo))
