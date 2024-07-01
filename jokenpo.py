from random import randint
from time import sleep

cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'limpa': '\033[m'}

while True:
    item = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0, 2)

    print('\nVamos jogar PEDRA, PAPEL E TESOURA')

    print('''
OPÇÔES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
[x] Fim de Jogo
''')

    jogador = int(input('Qual é a sua jogada? '))

    if jogador < 0 or jogador > 2:
        break

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
        print(f'{cores["azul"]}EMPATE{cores["limpa"]}')
    else:
        if computador == 0 and jogador == 1:
            print(f'{cores["verde"]}JOGADOR{cores["limpa"]} vence')
        elif computador == 1 and jogador == 0:
            print(f'{cores["vermelho"]}COMPUTADOR{cores["limpa"]} vence')
        elif computador == 2 and jogador == 0:
            print(f'{cores["verde"]}JOGADOR{cores["limpa"]} vence')
        elif computador == 0 and jogador == 2:
            print(f'{cores["vermelho"]}COMPUTADOR{cores["limpa"]} vence')
        elif computador == 2 and jogador == 1:
            print(f'{cores["vermelho"]}COMPUTADOR{cores["limpa"]} vence')
        else:
            print(f'{cores["verde"]}JOGADOR{cores["limpa"]} vence')
print('\nFIM DE JOGO')