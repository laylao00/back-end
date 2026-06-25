from random import randint
from time import sleep
print('''Suas opções
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogada = int(input('Qual sua jogada?'))
jogadapc = randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-=-'*10)
print(f'''Computador jogou {itens[jogadapc]}
Jogador jogou {itens[jogada]}''')
print('-=-'*10)
if jogadapc == 0 and jogada == 2 or jogadapc == 1 and jogada == 0 or jogadapc == 2 and jogada == 1:
    print('Computador venceu!')
elif jogada == 0 and jogadapc == 2 or jogada == 1 and jogadapc == 0 or jogada == 2 and jogadapc == 1:
    print('Jogador venceu! Parábens.')
else:
    print('Empate técnico.')
