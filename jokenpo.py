from random import randint
from time import sleep

item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('Vamos jogar PEDRA, PAPEL E TESOURA')
sleep(1)

print('''
OPÇÔES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
sleep(1)

jogador = int(input('Qual é a sua jogada? '))

print('\nJO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
sleep(0.7)

print(f'''
O computador escolheu {item[computador]}
O jogador escolheu {item[jogador]}
''')

if computador == jogador:
    print('EMPATE')
else:
    if computador == 0 and jogador == 1:
        print('JOGADOR vence')
    elif computador == 1 and jogador == 0:
        print('COMPUTADOR vence')
    elif computador == 2 and jogador == 0:
        print('JOGADOR vence')
    elif computador == 0 and jogador == 2:
        print('COMPUTADOR vence')
    elif computador == 2 and jogador == 1:
        print('COMPUTADOR vence')
    else:
        print('JOGADOR vence')