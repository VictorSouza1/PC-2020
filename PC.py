import pprint

B = [28,79,314,273,240,390,339,330,331,204,231,212]


A = [[0,0,10,5,6,7,0,0],
	[0,20,20,21,14,4,0,0],
	[90,65,82,64,10,3,0,0],
	[90,101,12,49,14,7,0,0],
	[90,29,46,48,20,7,0,0],
	[90,101,92,83,20,4,0,0],
	[90,65,80,84,15,5,0,0],
	[90,92,82,53,11,2,0,0],
	[90,101,79,47,5,9,0,0],
	[90,47,19,28,20,0,0,0],
	[90,20,35,86,0,0,0,0],
	[90,92,30,0,0,0,0,0]]
    
li = 2
ls = 3



def InicializaMatriz (n):
    M = []
    linha = []
    for i in range (n) :
        linha = []
        for j in range (n):
            linha.append(0)
        M.append(linha)
    return M

def PreencherDiagonalPrincipalCom1s (M):
    for i in range (len(M)):
        for j in range (len(M)):
            if i == j :
                M[i][j] = 1
    return

def TorcarLinhas (M, l1, l2):
    temp = M [l1]
    M[l1] = M [l2]
    M[l2] = temp
    return 

def parseTrocarLinhas (l1, l2):
    global A
    for i in range (len(A)):
        temp = parserAcesso(l1, i)
        parserEscrita(l1, i, parserAcesso(l2,i))
        parserEscrita(l2, i, temp)
        

def parserAcesso (m, n):
    global li
    global A
    if (n - m + li) < 0:
        return 0
    if (n - m + li) >= len(A[0]):
        return 0
    return A[m][n - m + li] 
    


def parserEscrita (m, n, valor):
    global li
    global A
    if (n - m + li) < 0:
        return
    if (n - m + li) >= len(A[0]):
        return
    A[m][n - m + li] = valor

    return

def LU ():
    global A
    global li
    global ls
    pp = pprint.PrettyPrinter()
    L = InicializaMatriz(len(A))
    for c in range (len(A)):
        
        max = abs(parserAcesso(c , c))                          #pivô
        Lmax = c
        
        for l in range (len(A)-c):              # Achar o menor elemento que pode ser um pivô
            if abs(parserAcesso(l+c, c)) > max:
                Lmax = l+c
                max = parserAcesso(l+c,c)
 
        
        parseTrocarLinhas(Lmax, c)                    # Trocar linha do pivô para posiciona-la corretamente
        TorcarLinhas(B, Lmax, c)                    # Realizar mesma troca no matriz B  
        TorcarLinhas(L, Lmax, c)                    # Realizar mesma troca no matriz L              
        for i in range (len(A)-c-1):            #  Fatorçao LU
            coef = parserAcesso(i+1+c, c) / parserAcesso(c, c)
            L[i+1+c][c] = coef                  # adicionando os elementos da matriz L (matriz de coeficientes) ja na posição correta
            for j in range (len(A)):            # zerando/operando sobre uma linha
                parserEscrita(i+1+c,j, parserAcesso(i+1+c, j) - coef * parserAcesso(c,j))
            
        
 

    PreencherDiagonalPrincipalCom1s(L)

    print('matriz a ')
    pp.pprint(A)
    print('matriz l ')
    pp.pprint(L)
    print('matriz b ')
    pp.pprint(B)

    return


if __name__ == "__main__":

    LU ()
    

