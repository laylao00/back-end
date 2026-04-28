import random
alunos = ['laylon','renan','thiago','josimar']
escolhido = random.choice(alunos)
print('O Aluno que vai apagar o quadrado é o {}'.format(escolhido))

from random import choice
aln1= str(input('Qual o nome do seu aluno?'))
aln2= str(input('Qual o nome do seu aluno?'))
aln3= str(input('Qual o nome do seu aluno?'))
aln4= str(input('Qual o nome do seu aluno?'))
lista = [aln1,aln2,aln3,aln4]
escolhido = choice(lista)#escolhe alguem da lista
print('O escolhido para limpar o quadro é o {}'.format(escolhido))
