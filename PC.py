import pprint

A = [[0,0,10,5,6,7],
	[0,20,20,21,14,4],
	[90,65,82,64,10,3],
	[90,101,12,49,14,7],
	[90,29,46,48,20,7],
	[90,101,92,83,20,4],
	[90,65,80,84,15,5],
	[90,92,82,53,11,2],
	[90,101,79,47,5,9],
	[90,47,19,28,20,0],
	[90,20,35,86,0,0],
	[90,92,30,0,0,0]]

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

def parserAcesso (A, m, n):
    global li
    return A[m][n - m + li + 1] 
    


def parserEscrita (m, n):
    pass

def LU (A,B):
    pp = pprint.PrettyPrinter()
    L = InicializaMatriz(len(A))


    pp.pprint(A)


    for c in range (len(A)):
        
        max = A[c][c]                           #pivô
        Lmax = c
        for l in range (len(A)-c):              # Achar o menor elemento que pode ser um pivô
            if abs(A[l+c][c]) > max:
                Lmax = l+c
                max = A[l+c][c]

        print('pivo = ', max, 'linha do pivo = ', Lmax)        
        TorcarLinhas(A, Lmax, c)                    # Trocar linha do pivô para posiciona-la corretamente
        TorcarLinhas(B, Lmax, c)                    # Realizar mesma troca no matriz B  
        TorcarLinhas(L, Lmax, c)                    # Realizar mesma troca no matriz L              
        pp.pprint(A)

        for i in range (len(A)-c-1):            #  Fatorçao LU
            coef = A[i+1+c][c] / A[c][c]
            L[i+1+c][c] = coef                  # adicionando os elementos da matriz L (matriz de coeficientes) ja na posição correta
            print('coeficiente = ', A[i+1+c][c], '/', A[c][c], '=', coef)
            for j in range (len(A)):            # zerando/operando sobre uma linha
                print('calculando : ', A[i+1+c][j], '- (', coef, ') * ', A[c][j], ' = ', A[i+1+c][j] - coef * A[c][j])
                A[i+1+c][j] = A[i+1+c][j] - coef * A[c][j]

        
 

    PreencherDiagonalPrincipalCom1s(L)

    print('matriz a ')
    pp.pprint(A)
    print('matriz l ')
    pp.pprint(L)
    print('matriz b ')
    pp.pprint(B)
    
    return
        

def LUnova ():
    global A
    global li
    global ls

    pp = pprint.PrettyPrinter()
    L = InicializaMatriz(len(A))

    for j in range(len(A[0])):
        print (A[0][j-0+li])
    #pp.pprint(A)

    '''
    for c in range (len(A)):
        
        max = A[c][c]                           #pivô
        Lmax = c
        for l in range (len(A)-c):              # Achar o menor elemento que pode ser um pivô
            if abs(A[l+c][c]) > max:
                Lmax = l+c
                max = A[l+c][c]

        print('pivo = ', max, 'linha do pivo = ', Lmax)        
        TorcarLinhas(A, Lmax, c)                    # Trocar linha do pivô para posiciona-la corretamente
        TorcarLinhas(B, Lmax, c)                    # Realizar mesma troca no matriz B  
        TorcarLinhas(L, Lmax, c)                    # Realizar mesma troca no matriz L              
        pp.pprint(A)

        for i in range (len(A)-c-1):            #  Fatorçao LU
            coef = A[i+1+c][c] / A[c][c]
            L[i+1+c][c] = coef                  # adicionando os elementos da matriz L (matriz de coeficientes) ja na posição correta
            print('coeficiente = ', A[i+1+c][c], '/', A[c][c], '=', coef)
            for j in range (len(A)):            # zerando/operando sobre uma linha
                print('calculando : ', A[i+1+c][j], '- (', coef, ') * ', A[c][j], ' = ', A[i+1+c][j] - coef * A[c][j])
                A[i+1+c][j] = A[i+1+c][j] - coef * A[c][j]

        
 

    PreencherDiagonalPrincipalCom1s(L)

    print('matriz a ')
    pp.pprint(A)
    print('matriz l ')
    pp.pprint(L)
    print('matriz b ')
    pp.pprint(B)
    '''
    return


if __name__ == "__main__":
    #A = [[2, 1, 1, 0], [4, 3, 3, 1], [8, 7, 9, 5], [6, 7, 9, 8]]
    #B = [1, 2, 4, 5]

    #A =[[1,-3,2], [-2, 8, -1], [4, -6, 5]]
    #B = [11, -15, 29]

    LUnova ()