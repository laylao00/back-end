print("="*11 + "LOJAS LIMA"+"="*11)

preco = float(input("Preço das compras"))
print ('''FORMAS DE PAGAMENTO''')
print ('[1] (à vista dinheiro/cheque)')
print ('[2] (à vista no cartão)')
print ('[3] (2x no cartão)')
print ('[4] (3x ou mais no cartão)')
pagamento = int(input("Qual é a opção? "))
if pagamento == 1:
    desconto = preco (preco*0.1)
    print("Sua compra com o desconto a vista fica R${}".format(desconto))

elif pagamento == 2:
    desconto = preco (preco*0.05)
    print("Sua compra a vista no cartão fica R${}".format(desconto))
elif:
    cartao = preco/2
    print("Sua compra parcelada no cartão fica 2x de {}".format(cartao))
elif pagamento == 4:
    parcela = int(input("Digite o número de parcelas "))
    juros = preco + (preco*0.2)
    total = juros/parcela
    print("A sua compra no cartão vai ser feita em {} parcelas e o valor com juros de cada parcela fica {}".format
(parcela, total))
