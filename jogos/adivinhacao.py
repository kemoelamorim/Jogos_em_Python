from random import randrange

# Função chama o cabeçalho
def cabecalho():
    print('''
    *******************************
    ***** Jogo da Adivinhação *****
    *******************************
    ''')

def nivel_do_jogo():
    print('''
    Escolha um nível de Dificuldade
    (1) Fácil (2) Médio (3) Difícil
    ''')

# Função chama o rodapé
def rodape():
    print('''
    *******************************
    ********* Fim do jogo *********
    *******************************
    ''')


# Printando Cabeçalho
cabecalho()


# Definindo número secreto
numero_secreto = randrange(0, 100)

# Nivel do jogo 
nivel_do_jogo()
nivel = int(input('Digite o nível de dificuldade: '))

# Definindo tentativas
tentativa = 0
while tentativa == 0:
    if nivel == 1:
        nivel = 'Fácil'
        tentativa = 5
        print(f'')
    elif nivel == 2:
        nivel = 'Médio'
        tentativa = 3
    elif nivel == 3:
        nivel = 'Difícil'
        tentativa = 2
    else:
        nivel_do_jogo()
        nivel = int(input('Digite o nível de dificuldade: '))
        tentativa = 0
    tentativas = tentativa

# Laço de tentativas
rodada = 1
while tentativas >= rodada:
    print(f'Nível: {nivel} Rodada: {rodada}  Tentativas: {tentativas}')
    # Entrada de Dados
    chute_str = input('Digite um numero: ')
    print('\nVocê digitou {}'.format(chute_str))
    chute = int(chute_str)

    # Verificação 
    acertou = chute == numero_secreto
    menor   = chute <  numero_secreto
    maior   = chute >  numero_secreto

    # Saída
    if acertou:
        print('Parabéns, você acertou!\n')
        break
    else:
        if maior:
            print('Você errou, seu chute foi maior que o número secreto!\n')
        elif menor:
            print('Você errou, seu chute foi menor que o número secreto!\n')

    rodada += 1  # somando + uma tentativa

# Printando Rodapé
rodape()
