def geraTabuleiro():
    M = []
    linha = []
    for i in range(3):
        linha.append(' . ')
        M.append(linha)
    return M

def imprimeTabuleiro(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end='')
        print('\n')

def jogar(tabuleiro, jogador, linha, coluna):
    if jogador == 1:
        if tabuleiro[linha-1][coluna-1] == ' . ':
            tabuleiro[linha-1][coluna-1] = ' X '
            return tabuleiro, True
        else:
            print('Jogada Inválida')
            return tabuleiro, False
    else:
        if tabuleiro[linha-1][coluna-1] == ' . ':
            tabuleiro[linha-1][coluna-1] = ' O '
            return tabuleiro, True
        else:
            print('Jogada Inválida')
            return tabuleiro, False 
    
def main():
    flag = False
    jogada = 0
    tabuleiro = geraTabuleiro()
    while flag == False:
        imprimeTabuleiro(tabuleiro)
        if jogada%2 == 0:
            jogador = 1
            jogAL = int(input('Linha: '))
            jogAC = int(input('Coluna: '))
            jogar(tabuleiro, jogador, jogAL, jogAC)
        else:
            jogador = 2
            jogBL = int(input('Linha: '))
            jogBC = int(input('Coluna: '))
            jogar(tabuleiro, jogador, jogBL, jogBC)
        jogada += 1

main()
