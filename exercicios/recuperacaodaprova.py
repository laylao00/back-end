1)r;
from random import randint
numeroaleatorio = randint(1,25)
print(numeroaleatorio)

2)r;
A função Ceil ou mais conhecido como Ceiling serve para arredondar um número decimal para o número inteiro maior ou mais próximo possível.

A função Trunc ou Truncate, serve para cortar depois da vírgula, transformando de um número real (float) para um número inteiro (int)

A função Sqrt ou Square Root serve para calcular a raiz quadrada de um número, caso a pessoa que esteja codando não queira utilizar a fórmula ''x/0,5".

E eles pertencem a biblioteca math.

3)r;
dias = int(input('Por quantos dias, o carro foi usado?'))
km = float(input('Quantos km foram rodados?'))
diaria = dias*47
percurso = km*0.25
custo = diaria+percurso 
print('O total a pagar é de R${}'.format(custo))

4)r;
salario = float(input('Qual seu salário?'))
aumento = salario + (salario * 12/100)
print('O seu salário é {:.2f}, mas com o aumento ficou {:.2f}.'.format(salario,aumento))
