import pprint

def InicializaMatriz (n):
    M = []
    linha = []
    for i in range (n) :
        linha = []
        for j in range (n):
            linha.append(0)
        M.append(linha)
    return M

def CriaMatriz_L (n):
    M = []
    linha = []
    for i in range (n):
        linha = []
        for j in range (n):
            if i == j :
                linha.append(1)
            else:
                linha.append(0)
        M.append(linha)
    return M

def TorcarLinhas (M, l1, l2):
    temp = M [l1]
    M[l1] = M [l2]
    M[l2] = temp
    return 


def LU (A,B):
    pp = pprint.PrettyPrinter()
    L = CriaMatriz_L(len(A))


    pp.pprint(A)


    for c in range (len(A)):
        
        max = A[c][c]                           #pivô
        Lmax = c
        for l in range (len(A)-c):              # Achar o menor elemento que pode ser um pivô
            if abs(A[l+c][c]) > max:
                #print(A[l+c][c], 'entrou')
                Lmax = l+c
                max = A[l+c][c]

        print('pivo = ', max, 'linha do pivo = ', Lmax)        
        TorcarLinhas(A, Lmax, c)                    # Trocar linha do pivô para posiciona-la corretamente
        TorcarLinhas(B, Lmax, c)                    # Realizar mesma troca no matriz B               
        pp.pprint(A)

        for i in range (len(A)-c-1):            # eliminação de gauss
            coef = A[i+1+c][c] / A[c][c]
            L[i+1+c][c] = coef                  # adicionando os elementos da matriz L (matriz de coeficientes) ja na posição correta
            print('coeficiente = ', A[i+1+c][c], '/', A[c][c], '=', coef)
            for j in range (len(A)):            # zerando/operando sobre uma linha
                print('calculando : ', A[i+1+c][j], '- (', coef, ') * ', A[c][j], ' = ', A[i+1+c][j] - coef * A[c][j])
                A[i+1+c][j] = A[i+1+c][j] - coef * A[c][j]
            
        pp.pprint(A)
        pp.pprint(L)
        pp.pprint(B)
        
 

        
    
    return
        



if __name__ == "__main__":
    #A = [[2, 1, 1, 0], [4, 3, 3, 1], [8, 7, 9, 5], [6, 7, 9, 8]]
    #B = [1, 2, 4, 5]


    A = [[1,-3,2],[-2,8,-1],[4,-6,5]]
    B = [11,-15,29]
    LU (A,B)