def leArquivo(arquivo):
    arq = open(arquivo, 'r')
    tamanho = arq.readline()
    tamanho = tamanho.rstrip()
    tamanho = int(tamanho)
    vetLinhas = [0]*tamanho
    for i in range(tamanho):
        linha = arq.readline()
        linha = linha.rstrip()
        vetLinha = linha.split(' ')
        for j in range(tamanho):
            vetLinha[j] = int(vetLinha[j])
        vetLinhas[i] = vetLinha
    return vetLinhas

def imprimeMatriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(' ', M[i][j],' ', end='')

        print('\n')

def verificaQuadrado(M):
    somaLinha = 0
    somaColuna = 0
    i = 0
    while i < len(M):
        j = 0
        while j < len(M):
            somaLinha = somaLinha+M[i][j]
            j += 1
        i +=1
    if soma  
arquivo = leArquivo('quadradomagico.txt')
imprimeMatriz(arquivo)
arquivo.close()

'''
EXEMPLO
3  TAMANHO DO QUADRADO
8 1 6 1ª LINHA DO QUADRADO
3 5 7 2ª LINHA DO QUADRADO
4 9 2 3ª LINHA DO QUADRADO
'''
