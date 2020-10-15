#prod escalar
import numpy as np
'''v1 = [float(x) for x in input().split()]
v2 = [float(x) for x in input().split()]
res = np.dot(v1, v2)
print('%.2f' % res)'''
#contar quantos valores
'''l = input().split()
r = []
for x in l:
    if x not in r:
        r.append(x)
print(len(r))'''
#indice da primeira posicão que o n ta
'''V = input().split()
n = input()
resp = -1
if n in V:
    resp = V.index(n)
print(resp)'''
#alternar os elem de duas listas
'''L1 = input().split()
L2 = input().split()
L =[]
n1, n2 = len(L1), len(L2)
n = min(n1,n2)

for i in range(n):
    e1 = L1.pop(0)
    e2 = L2.pop(0)
    L.append(e1)
    L.append(e2)
if len(L1):
    L += L1
else:
    L += L2

resp = ' '.join(L)
print(resp)'''