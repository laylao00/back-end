num1 = int(input('Escolha um número'))
num2 = int(input('Escolha um número'))
num3 = int(input('Escolha um número'))

maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num2 and num3>num2:
    maior = num3

menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))
