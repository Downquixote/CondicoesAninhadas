# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os: 
# - O PRIMEIRO VALOR é maior
# - O SEGUNDO VALOR é maior.
# - NÂO EXISTE valor maior, os dois são IGUAIS.

a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor inteiro: '))

if a > b:
    print('O primeiro valor é maior!')
elif b > a:
    print('O segundo valor é maior!')
else: 
    print('Não há valor maior, os dois valores são iguais!')