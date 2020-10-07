# tabuada
'''n = int(input())
for i in range (1,11):
    m = n * i 
    print('{0} * {1} = {2}'.format(n, i, m))'''
#soma dos impares
'''x , y = input(). split()
x, y = int(x), int(y)
s = 0
for i in range(x,y):
    if (not (i % 2 == 0)):
        s +=i
print('{0}'.format(s))'''
#soma de riemman
'''n = int(input())
s = 0.0
for i in range (1 ,n):
    s += i/(n-(i-1))
t = s+n
print('%.48f' %t)'''
#horario do onibus
'''t = int(input())
h = 300
print('05:00')
while(h < 1435):
    h += t
    horas = int(h/60)
    minutos = h - horas*60 
    print('%02d:%02d' % (horas, minutos))'''
#todos os divisores
'''n = int(input())
c = 0
div = []
for i in range(2, n):
    if (n % i == 0):
         div.append(i)
         c +=1
if(c == 0):
    print('primo')
else:
    for j in div:
        print('%d'%j)'''
#mmc
'''def mdc(a, b):
    a, b= max(a,b), min(a, b)
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b

a, b = input().split()
a, b = int(a), int(b)
mmc = a * b / mdc(a,b)
print(mmc)'''
#aproximação de pi
'''n = int(input())
s = 0.0
for i in range(n+1):
    o = 8.0*i
    p = 16**(-i)
    s += p*((4.0/(o+1.0))-(2.0/(o+4.0))-(1.0/(o+5.0))-(1.0/(o+6.0)))
print('%.48f' % s)'''
#numero perfeito
'''n = int(input())
s = 0 
for i in range (1,n):
    if (n % i == 0):
        s +=i
if (s == n):
    v = True
else:
    v = False
print(v)'''
#numero de armstrong
'''n = input()
d = list(n)
num = []
s = 0.0
for i in d:
    num.append(int(i))
for i in num:
    s += i**n
if (s == n):
    v = True
else:
    v = False
print(v)'''
#esfera - coordenadas
'''import math
x, y, z, r = input().split()
x, y, z, r = float(x), float(y), float(z), float(r)
p = 0
for i in range(int(x - r), int(x + r + 1)):
    for j in range (int(y - r), int(y + r + 1)):
        for k in range (int(z - r), int(z + r + 1)):
            s = ((x - i)**2)+((y - j)**2)+((z-k)**2)
            d = math.sqrt(s)
            if d <= r:
                p +=1
print(p)'''