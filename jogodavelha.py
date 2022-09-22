def geraTabuleiro():
    M = []
    linha = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(' . ')
        M.append(linha)
    return M

def imprimeTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            print(tabuleiro[i][j], end='')
        print('\n')
    return tabuleiro

def jogar(tabuleiro, jogador, linha, coluna):
    while jogador == 1:
        if tabuleiro[linha-1][coluna-1] == ' . ':
            tabuleiro[linha-1][coluna-1] = ' X '
            return tabuleiro
        else:
            print('Posição Inválida')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            print('\n')


    while jogador == 2:
        if tabuleiro[linha-1][coluna-1] == ' . ':
            tabuleiro[linha-1][coluna-1] = ' O '
            return tabuleiro
        else:
            print('Posição Inválida')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            print('\n')
            
def verificaGanhador(tabuleiro, jogador):    
            
def main():
    flag = False
    jogada = 0
    tabuleiro = geraTabuleiro()
    while flag == False:
        imprimeTabuleiro(tabuleiro)
        if jogada%2 == 0:
            jogAL = int(input('Linha: '))
            jogAC = int(input('Coluna: '))
            print('\n')
            jogador = 1
            jogar(tabuleiro, jogador, jogAL, jogAC)
        else: 
            jogBL = int(input('Linha: '))
            jogBC = int(input('Coluna: '))
            print('\n')
            jogador = 2
            jogar(tabuleiro, jogador, jogBL, jogBC)
        jogada += 1

main()
