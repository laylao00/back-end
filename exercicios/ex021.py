from random import shuffle
aln1= str(input('Qual o nome do seu aluno?'))
aln2= str(input('Qual o nome do seu aluno?'))
aln3= str(input('Qual o nome do seu aluno?'))
aln4= str(input('Qual o nome do seu aluno?'))
lista = [aln1,aln2,aln3,aln4]
shuffle(lista)#embaralha a lista
print('Quem vão apresentar são o {}'.format(lista))
