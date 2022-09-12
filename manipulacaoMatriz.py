import random
def geraMatriz(m,n):
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(random.randint(1,100))
        M.append(linha)
    return M

def geraMatrizquad(m):
    M = []
    for i in range(m):
        linha = []
        for j in range(m):
            linha.append(random.randint(1,100))
        M.append(linha)
    return M

def buscaMario(M):
    maior = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] > maior:
                maior = M[i][j]
    return maior

def diagonalPrincipal(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i != j and M[i][j] != 0:
                return False
    return True

def traco(M):
    soma = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i == j:
                soma += M[i][j]
    return soma            

def main():
    m = random.randint(3,10)
    n = random.randint(3,10)
    M1 = [[1,0,0],[0,2,0],[0,0,3]]
    M = geraMatrizquad(m)
    print(traco(M))
    print(M)

main()
