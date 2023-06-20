# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não deverá exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor da sua renda mensal? '))
anos = int(input('Quantos anos irá pagar? '))

parcela = anos * 12
mensal = valor / parcela

if mensal > (salario * 30 / 100):
    print('Empréstimo NEGADO, valor da parcela mensal maior que 30% do salario!')
    print('Valor da parcela: R${:.2f}'.format(mensal))
else: 
    print('Empréstimo PERMITIDO!')
    print('Valor da parcela: R$ {:.2f}'.format(mensal))
