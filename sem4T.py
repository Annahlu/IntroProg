#1 - soma, qts vezes o 9 apareceu, maior, posições do maior
''' V = [int(x) for x in input().split()]
s = 0
maior = 0
c = 0
P =[]
for i in range(0,len(V)):
  s += V[i]
  if V[i] == 9:
    c+=1
  if V[i] > maior:
    maior = V[i]
print(s)
print(c)
print(maior)
for i in range(0,len(V)):
  if V[i] == maior:
    P.append(i)
P = [str(x) for x in P]
r = ' '.join(P)
print(r)
'''
#2
'''L = [int(x) for x in input().split()]
u = L.pop()
NL = [u] + L
NL = [str(i) for i in NL]
NL = ' '.join(NL)
print(NL)
'''
#3
'''V = input().split()
V = V[::-1]
V = ' '.join(V)
print(V)'''
#4
'''V = []
qtdc, sp, si, i = 0, 0, 0, 0
n = 1
while(n >= 0):
    n = int(input())
    V.append(n)
V.pop()
for i in range(0,len(V)):
    if(V[i] > 5):
        qtdc +=1
    if( not V[i] % 2):
        sp += V[i]
    else:
        si += V[i]
print(qtdc)
print(sp)
print(si)
print(len(V))
V = [str(x) for x in V]
r = ' '.join(V)
print(r)'''
#5
'''dt, m ,n = input().split()
dt , m, n = float(dt), int(m), int(n)
X, Y, Z, Vx, Vy, Vz, R = [], [], [], [], [], [], []
xf, yf, zf = 0.0, 0.0, 0.0
for i in range (0,n):
    x, y, z, vx, vy, vz = input().split()
    x, y, z, vx, vy, vz = float(x),float(y),float(z),float(vx), float(vy), float(vz)
    xf,yf,zf = x,y,z
    for j in range(0,m):
        xf += vx * dt
        yf += vy * dt
        zf += vz * dt
    print('%.2f %.2f %.2f'%(xf, yf,zf))'''
#6
'''V = [float(x) for x in input().split()]
s, m = 0,1
for i in range(len(V)):
    s += V[i]
    m *= V[i]
    print('%.2f %.2f' %(s, m))
'''
#7
'''V = [int(x) for x in input().split()]
V2 = []
V3 = []
a, c = 0, 0
def isin(V,v):
    for i in V:
        if (i == v):
            return True
    return False
for i in V:
    if (i >=0):
        V2.append(i)
for i in V2:
     if (not isin(V3,i)):
        V3.append(i)
V3 = [str(x) for x in V3]
r = ' '.join(V3)
print(r)'''
#8
'''import math
import numpy as np
N = [float(x) for x in input().split()]
N = np.sort(N)
s, sd = 0, 0
for i in N:
    s+=i
mean = s/float(len(N))
if(len(N) % 2 == 0):
    median = (N[int((len(N)/2)-1)]+N[int(len(N)/2)])/2
else:
    median = N[int(len(N)/2)]
for i in N: 
    sd += (i-mean)**2
sd /= len(N)
sd = math.sqrt(sd)
print('%.2f %.2f %.2f' %(mean, median, sd))'''
#9
'''import numpy as np
def isin(V,v):
    for i in V:
        if (i == v):
            return True
    return False
def unique(V):
    V2 = []
    for i in V:
        if (not isin(V2,i)):
            V2.append(i)
    return V2
V = [int(x) for x in input().split()]
V2 = np.sort(unique(V))
V3 = []
for v in V2:
    V3.append(V.count(v))
for i in range(0,len(V3)):
    if (V3[i] > 1):
        print('%d %d'%(V2[i], V3[i]))
'''
#10
'''
V = [float(i) for i in input().split()]
p = [float(i) for i in input().split()]
i, j = 0, -2
OX = (V[0] + V[2] + V[4])/3 
OY = (V[1] + V[3] + V[5])/3
r = 'N'
while i < len(p):
	j = -2
	r = 'N'
	OPX = p[i] - OX
	OPY = p[i+1] - OY
	while j+3 < len(V):
		XV1 = V[j] - OX
		YV1 = V[j+1] - OY
		XV2 = V[j+2] - OX
		YV2 = V[j+3] - OY
		alfa = (OPX*YV2 - OPY*XV2)/(XV1*YV2 - XV2*YV1)
		beta = (OPX*YV1 - OPY*XV1)/(YV1*XV2 - YV2*XV1)
		if(alfa + beta <= 1 and alfa >= 0 and beta >= 0):
			r = "S"
		j += 2
	print(r)
	i += 2
	'''    

