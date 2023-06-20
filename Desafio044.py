# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# Á vista DINHEIRO/BOLETO: 10% de desconto.
# Á vista no CARTÃO: 5% de desconto.
# Em até 2X NO CARTÃO: Preço normal.
# 3X OU MAIS no cartão: 20% de juros.

from random import uniform

produto = str(input('Digite o produto que deseja: ')).strip()
valor = round(uniform(1500.0, 10000.0), 2)
print('Valor do {}: R${:.2f}'.format(produto, valor))

print('='*40)

print('''Selecione a forma de pagamento:
[1] Á vista Pix ou Boleto: 10% de cashback.
[2] Á vista no cartão: 5% de cashback.
[3] Em até 2x sem juros no cartão.
[4] 3x ou mais no cartão: 20% de juros.''')

print('='*40)

opcao = int(input('Digite aqui a opção que deseja: '))
if opcao == 1:
    desconto10 = valor * (10 / 100)
    new1 = valor - desconto10 
    print('Ebaaaa! Você escolheu Pix ou boleto, acaba de ganhar 10% de cashback com essa forma de pagamento.')
    print('10% de cashback: R${:.2f}'.format(desconto10))
    print('Valor do produto com cashback: R${:.2f}'.format(new1))
elif opcao == 2:
    desconto5 = valor * (5 / 100)
    new2 = valor - desconto5
    print('Obaaaa! Você escolheu pagar á vista no cartão, com essa forma de pagamento você acaba de ganhar 5% de cashback.')
    print('5% de cashback: R${:.2f}'.format(desconto5))
    print('Valor do produto com cashback: R${:.2f}'.format(new2))
elif opcao == 3:
    parcela = valor / 2
    print('Você escolheu pagar em 2x no cartão.')
    print('Valor total do produto: R${:.2f}'.format(valor))
    print('1º parcela: R${:.2f}'.format(parcela))
    print('2º parcela: R${:.2f}'.format(parcela))
elif opcao == 4:
    print('Você escolheu pagar em 3x no cartão. Essa forma de pagamento cobra 20% de juros.')
    parcela20 = int(input('Digite a quantidade de parcelas: '))
    if parcela20 < 3:
        print('Opção Inválida!')
    else:
        juros = valor * (20 / 100)
        new3 = juros + valor
        jurosMensal = new3 / parcela20
        print('Você quer parcelar em {} vezes.'.format(parcela20))
        print('Novo valor do produto: R${:.2f}'.format(new3))
        print('Valor das {} parcelas: R${:.2f}'.format(parcela20, jurosMensal))
else:
    print('Opção inválida!')

