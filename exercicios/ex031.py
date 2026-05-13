viagem = float(input('Qual é a distância para sua viagem?'))
curta = 0.5 * viagem
longa = 0.45 * viagem
print('Você está prestes a começar uma viagem de {}km'.format(viagem))
if viagem<= 200:
    print('E o preço da viagem será igual a R${}'.format(curta))
else:
    print('E o preço da viagem será igual a R${:.2f}'.format(longa))
