import random
def jogar_forca():
    # Função chama o cabeçalho
    def cabecalho():
        print('''
        *******************************
        ******** Jogo da Forca ********
        *******************************
        ''')

    cabecalho()

    arquivo = open("jogos/palavras_secretas/palavras.txt","r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    posicao = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao].upper()
    print(palavra_secreta)

    acertou = False
    enforcou = False
    letras_acertadas = ['_' for letra in palavra_secreta] 
    print(letras_acertadas)
    erros = 0

    while not acertou and not enforcou:
        
        chute = input('Digite seu chute: ').strip().upper()
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                    print('Encontramos a letra "{}" na posição "{}"'.format(letra, index))
                index += 1 
        else:
            erros += 1
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        
        if acertou:
            print('Você acertou!')
        else:
            print('Você errou!')

if __name__ == '__main__':
    jogar_forca()