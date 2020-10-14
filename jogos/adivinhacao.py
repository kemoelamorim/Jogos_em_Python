# Função chama o cabeçalho
def cabecalho():
    print('''
    *******************************
    ***** Jogo da Adivinhação *****
    *******************************
    ''')
cabecalho()

# Entrada de Dados
numero_secreto = 33
chute = int(input('Digite um numero: '))

# Verificação e saída
if chute == numero_secreto:
    print('Você acertou!')
else:
    print('Você errou!')



