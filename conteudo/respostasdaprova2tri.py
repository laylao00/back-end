Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 15 primeiros termos dessa progressão.
*
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Os 15 primeiros termos da PA são: ')
for i in range(15):
    trm = a1 + i * r
    print(trm, end=' ')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão: '))
decimo = primeiro + 15 * razao #formula de PA
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' -> ')
print('Acabou')

Desenvolva um programa que leia 10 números inteiros e mostre a soma apenas daqueles que forem ímpares. Se o valor digitado for par desconsiderar.

*
soma = 0
cont = 0
for c in range(1,7):
   num = int(input(f'Digite o {c} valor'))
   if num%3 == 0:
          soma += num
          cont = cont +1
print(f'Você informou {cont} números ímpares e a soma deles são {soma})

O que faz o laço de repetição for e qual a sua sintaxe?
*
O laço de repetição for em Python é usado para repetir um bloco de código várias vezes, percorrendo elementos de uma sequência.
Sintaxe: for + variável de controle + in + range(x,y) sendo x o início e y o final

Faça um programa que calcule a soma entre todos os números pares que são múltiplos de 6 e que se encontram no intervalo de 1 até 300
*
s = 0
cont = 0
for c in range(2,301,2)
   if c%6 == 0:
       cont += 1
       s += c
print(f'A soma de todos os {cont} valores solicitados é {s})

