# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
m = (a + b) / 2

if m < 5.0:
    print('Média {}'.format(m))
    print('REPROVADO!')
elif m > 5.0 and m < 6.9:
    print('Média {}'.format(m))
    print('RECUPERAÇÃO!')
else: 
    print('Média {}'.format(m))
    print('APROVADO!')