import pprint

L = []

A2 = [[10,5,6,7,0,0,0,0,0,0,0,0],
	[20,20,21,14,4,0,0,0,0,0,0,0],
	[90,65,82,64,10,3,0,0,0,0,0,0],
	[0,90,101,12,49,14,7,0,0,0,0,0],
	[0,0,90,29,46,48,20,7,0,0,0,0],
	[0,0,0,90,101,92,83,20,4,0,0,0],
	[0,0,0,0,90,65,80,84,15,5,0,0],
	[0,0,0,0,0,90,92,82,53,11,2,0],
	[0,0,0,0,0,0,90,101,79,47,5,9],
	[0,0,0,0,0,0,0,90,47,19,28,20],
	[0,0,0,0,0,0,0,0,90,20,35,86],
	[0,0,0,0,0,0,0,0,0,90,92,30]]

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



def InicializaMatrizL ():
    global A
    global L
    M = []
    linha = []
    for i in range (len(A)) :
        linha = []
        for j in range (len(A[0])):
            linha.append(0)
        L.append(linha)
    return

def PreencherDiagonalPrincipalCom1s (M):
    for i in range (len(M)):
        for j in range (len(M)):
            if i == j :
                M[i][j] = 1
    return



def parseTrocarLinhas (M, l1, l2):
    global A
    for i in range (len(A)):
        temp = parserAcesso(M, l1, i)
        parserEscrita(M,l1, i, parserAcesso(M, l2,i))
        parserEscrita(M, l2, i, temp)
        

def parserAcesso (M , m, n):
    global li

    if (n - m + li) < 0:
        return 0
    if (n - m + li) >= len(M[0]):
        return 0
    return M[m][n - m + li] 
    


def parserEscrita (M , m, n, valor):
    global li
    if (n - m + li) < 0:
        return
    if (n - m + li) >= len(M[0]):
        return
    M[m][n - m + li] = valor

    return


def LUnova ():
    global A
    global L
    global li
    global ls

    pp = pprint.PrettyPrinter()
    InicializaMatrizL()
    print ("l é igual a ", L)

    for c in range (len(A)):
        
        max = abs(parserAcesso(A, c , c))                          #pivô
        Lmax = c
        
        for l in range (len(A)-c):              # Achar o menor elemento que pode ser um pivô
            if abs(parserAcesso(A, l+c, c)) > max:
                Lmax = l+c
                max = parserAcesso(A, l+c,c)

        #print('pivo = ', max, 'linha do pivo = ', Lmax)        
        
        parseTrocarLinhas(A, Lmax, c)                    # Trocar linha do pivô para posiciona-la corretamente
        #print ('primeiro A ficou ')
        #pp.pprint(A)
        #TorcarLinhas(B, Lmax, c)                    # Realizar mesma troca no matriz B  
        
        parseTrocarLinhas(L, Lmax, c)                    # Realizar mesma troca no matriz L              
     
        #pp.pprint(A)
        
        
        for i in range (len(A)-c-1):            #  Fatorçao LU
            coef = parserAcesso(A, i+1+c, c) / parserAcesso(A, c, c)
            parserEscrita(L, i+1+c, c, coef)             # adicionando os elementos da matriz L (matriz de coeficientes) ja na posição correta
            print ("Adicionando o coeficiente na posicao ", i+1+c, ",", c)
            print("cada passo de L : ")
            pp.pprint(L)
            #print('coeficiente = ', parserAcesso(i+1+c, c), '/', parserAcesso(c, c), '=', coef)
            
            for j in range (len(A)):            # zerando/operando sobre uma linha
                #print('calculando : ', parserAcesso(i+1+c, j) , '- (', coef, ') * ',parserAcesso(c,j) , ' = ', parserAcesso(i+1+c, j) - coef * parserAcesso(c,j))
                parserEscrita(A , i+1+c,j, parserAcesso(A , i+1+c, j) - coef * parserAcesso(A , c,j))
            
        
 

    #PreencherDiagonalPrincipalCom1s(L)

    print('matriz a ')
    pp.pprint(A)
    print('matriz l ')
    pp.pprint(L)
    #print('matriz b ')
    #pp.pprint(B)

    return


if __name__ == "__main__":
    #A = [[2, 1, 1, 0], [4, 3, 3, 1], [8, 7, 9, 5], [6, 7, 9, 8]]
    #B = [1, 2, 4, 5]

    #A =[[1,-3,2], [-2, 8, -1], [4, -6, 5]]
    #B = [11, -15, 29]

    #A= [[2,1,5], [4,4,-4], [1,3,1]]
    #B = [11, -15, 29]
    
    #A = [[-8,1,-2],[-3,-1,7],[2,-6,-1]] 
    #B = [-20,-38,-34]
    LUnova ()
    
    #LU(A2,B)