from adivinhacao import jogar_adivinhacao
from forca import jogar_forca

def escolha_o_jogo():
    # Função escolhe o nível
    def nivel_do_jogo():
        print('''
        ** Escolha qual o Jogo **
        (1) Adivinhação (2) Forca
        ''')
    nivel_do_jogo()

    escolha_do_jogo = int(input('Digite sua escolha: '))

    if escolha_do_jogo == 1:
        print("Jogando jogo da Adivinhação...")
        jogar_adivinhacao()
    elif escolha_do_jogo == 2:
        print("Jogando jogo da Forca...")
        jogar_forca()

if __name__ == '__main__':
    escolha_o_jogo()