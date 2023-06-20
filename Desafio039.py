# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele AINDA VAI SE ALISTAR ao serviço militar.
# - Se é a HORA DE SE ALISTAR.
# - Se já PASSOU DO TEMPO do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

idade = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year - idade

if ano == 18: 
    print('Está na hora de se alisar!')
elif ano < 18:
    menor = 18 - ano
    print('Ainda não está no tempo de se alistar.')
    print('Faltam {} anos.'.format(menor))
else:
    maior = ano - 18
    print('Passou do tempo de se alistar!')
    print('Passaram {} anos.'.format(maior))
