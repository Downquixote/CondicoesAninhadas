# Crie um programa que jogue JOKENPÔ com você.

from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
pc = choice(opcoes)

print('O computador escolheu: ')

user = str(input('Digite "pedra", "papel" ou "tesoura" para jogar com a CPU: ')).lower().strip()

if user == pc:
    print('O computador escolheu: {}'.format(pc))
    print('Empate!')
elif (user == 'pedra' and pc == 'tesoura') or \
    (user == 'tesoura' and pc == 'papel') or \
    (user == 'papel' and pc == 'pedra'):
    print('O computador escolheu: {}'.format(pc))
    print('Você ganhou!')
else:
    print('O computador escolheu: {}'.format(pc))
    print('Você perdeu!')