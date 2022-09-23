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
arquivo = leArquivo('quadradomagico.txt')
imprimeMatriz(arquivo)
