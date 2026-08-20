from random import randint
print('Sou seu computador')
print('''Acabei de pensar em um número entre 0 e 10. Será que você consegue adivinhar qual foi?''')
palpite = int(input('Qual o seu palpite?'))
aleatorio = randint(0,10)
tentativas = 0
while aleatorio !=palpite:
    if aleatorio > palpite:
        palpite = int(input(('Mais... Tente denovo!')))
        tentativas +=1
    elif aleatorio < palpite:
        palpite = int(input('Menos... Tente denovo!'))
        tentativas +=1
tentativas +=1
print(f'Acertou com {tentativas} tentativas. Parábens!')
