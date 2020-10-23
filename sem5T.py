#multiplicação de matriz q ta dando errado
a1, a2, b1, b2 = input().split()
a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
A = []
B = []
if (a1 == 0 or a2 == 0 or b1 == 0 or b2 == 0):
    print('Incompatíveis')
else:
    for i in range(a1):
        L = [float(x) for x in input().split()]
        A.append(L)
    for i in range(b1):
        L = [float(x) for x in input().split()]
        B.append(L)
    if (a2 == b1):
        C = []
        for i in range(a1):
            row = []
            for j in range(b2):
                c = 0
                for k in range(b1):
                    c += A[i][k]*B[k][j]
                row.append(c)
            C.append(row)
            for L in C:
                for n in range(len(L)):
                    print('%.2f '%L[n],end="")
                    if( n < len(L)-1):
                        print(end = " ")
    else:
        print('Incompatíveis')