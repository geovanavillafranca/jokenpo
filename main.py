from random import randint
from time import sleep

print('--- Vamos jogar Jokenpo ---')
user = 0
maquina = 0
empates = 0
while True:
    itens = ('Tesoura', 'Papel', 'Pedra')
    #    0    ,    1   ,    2
    computador = randint(0, 2)
    print('''Suas opções:
    [0] Tesoura
    [1] Papel
    [2] Pedra ''')
    #agora o jogador escolhe sua jogada: entre o 0 até o 2
    jogador = int(input('Qual a sua jogada? '))
    if jogador < 3 and jogador >= 0:
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!!!')
        sleep(0.5)
        print('-=' * 11)
        print('Computador jogou {}' .format(itens[computador]))
        print('Jogador jogou {}' .format(itens[jogador]))
        print('-=' * 11)
        if computador == 0: #computador jogou tesoura
            if jogador == 0:
                empates += 1
                print('EMPATE')
            elif jogador == 1:
                maquina += 1
                print('COMPUTADOR VENCEU')
            elif jogador == 2:
                user += 1
                print('VOCÊ VENCEU')

        elif computador == 1: # computador jogou papel
            if jogador == 0:
                user += 1
                print('VOCÊ VENCEU')
            elif jogador == 1:
                empates += 1
                print('EMPATE')
            elif jogador == 2:
                maquina += 1
                print('COMPUTADOR VENCEU')

        elif computador == 2: #computador jogou pedra
            if jogador == 0:
                maquina += 1
                print('COMPUTADOR VENCEU')
            elif jogador == 1:
                user += 1
                print('VOCÊ VENCEU')
            elif jogador == 2:
                empates += 1
                print('EMPATE')
        opcao = str(input('Deseja jogar de novo?[S/N] ')).strip().upper()[0]
        while opcao not in 'SN':
            print('\033[31mERRO! Digite um opção válida.\033[m')
            opcao = str(input('Deseja jogar de novo?[S/N] ')).strip().upper()[0]
            sleep(0.5)

        if opcao == 'S':
            sleep(.5)
        elif opcao == 'N':
            print('Finalizando...')
            sleep(1)
            break

    else:
        print('\033[31mERRO! OPÇÃO NÃO EXISTE\033[m')
print('***' * 10)
print('------ TABELA DE PONTOS ------')
print(f'{"Você":<10} ', end='')
print(f'| {user:>15}')
print(f'{"Computador":<10} ', end='')
print(f'| {maquina:>15}')
print(f'{"Empates":<10} ', end='')
print(f'| {empates:>15}')
print('***' * 10)
if maquina > user:
    print('\033[35mO computador ganhou!!')
elif empates > maquina and empates > user:
    print('\033[35mNinguém ganhou')

elif maquina == user:
    print('\033[35mEmpate entre os jogadores')
else:
    print('\033[35mVocê ganhou!!!!')
