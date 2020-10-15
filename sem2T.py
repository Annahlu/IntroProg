import math as ma
#1 - formula de bhaskara
'''e = input()
a,b,c = e.split()
a,b,c= float(a), float(b), float(c)
d = (b**2) - (4*a*c)
if (d < 0):
    print('No real roots.')
elif (d == 0):
    x = (- b)/(2*a)
    print("%.2f"%(x))
else:
     x1 = (- b + ma.sqrt(d))/ (2*a)
     x2 =  (- b - ma.sqrt(d))/ (2*a)
     print("%.2f"%(x1))
     print("%.2f"%(x2))
'''
#2 - pos/neg impar/par
'''n = input()
n = float(n)
if (n % 2 == 0):
    print('Par')
else:
    print('Impar')
if(n < 0):
    print('Negativo')
elif(n == 0):
    print('Zero')
else:
    print('Positivo')'''
#3 - maior de 5
n1, n2, n3, n4, n5 = input().split()
n1, n2, n3, n4, n5 = float(n1), float(n2), float(n3), float(n4), float(n5)
maior = n1
menor = n1
n = [n1 , n2, n3, n4, n5]
for i in n:
    if(i > maior):
        maior = i
    elif(i < menor):
        menor = i
print('%.2f'%maior,' %.2f'%menor)
#4 - triangulo
import math as ma
'''x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
x3, y3 = float(x3), float(y3)
a = ma.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
b = ma.sqrt(((x3 - x2)**2)+((y3 - y2)**2))
c = ma.sqrt(((x3 - x1)**2)+((y3 - y1)**2))
if (a < b + c and b < a + c and c < a + b):
    print('triângulo')
    if (a == b and b == c):
      print('equilátero')
    elif((a == b and b != c ) or (a == c and b != a )):
      print('isóceles')
    else: 
      print('escaleno')
else: 
     print('não triângulo')'''
#5 - signo
'''d, m = input().split("/")
d, m = float(d), float(m)
if (m == 4):
    if(d >= 19 and d <= 30):
        print('Áries')
    elif(d >= 1 and d <= 18):
       print('Peixes')
elif(m == 5):
    if(d >= 1 and d <= 13):
        print('Áries')
    elif(d >= 14 and d<= 31):
        print('Touro')
elif(m == 6):
     if(d >= 1 and d <= 19):
        print('Touro')
     elif(d >= 20 and d<= 30):
        print('Gêmeos')
elif(m == 7):
     if(d >= 1 and d <= 20):
        print('Gêmeos')
     elif(d >= 21 and d<= 31):
        print('Câncer')
elif(m == 8):
     if(d >= 1 and d <= 9):
        print('Câncer')
     elif(d >= 10 and d<= 31):
        print('Leão')
elif(m == 9):
     if(d >= 1 and d <= 15):
        print('Leão')
     elif(d >= 16 and d<= 30):
        print('Virgem')
elif(m == 10):
     if(d >= 1 and d <= 30):
        print('Virgem')
     elif(d == 31):
        print('Libra')
elif(m == 11):
     if(d >= 1 and d <= 22):
        print('Libra')
     elif(d >= 23 and d<= 29):
        print('Escorpião')
     elif(d == 30):
        print('Serpentário')
elif(m == 12):
     if(d >= 1 and d <= 17):
        print('Serpentário')
     elif(d >= 18 and d<= 31):
        print('Sagitário')
elif(m == 1):
     if(d >= 1 and d <= 17):
        print('Sagitário')
     elif(d >= 19 and d<= 31):
        print('Capricórnio')
elif(m == 2):
     if(d >= 1 and d <= 15):
        print('Capricórnio')
     elif(d >= 16 and d<= 28):
        print('Aquário')
elif(m == 3):
     if(d >= 1 and d <= 12):
        print('Aquário')
     elif(d >= 13 and d<= 31):
        print('Peixes')'''
#6 - notação polonesa inversa
'''n1, n2, o = input().split()
n1, n2 = float(n1), float(n2)
if (o == '+'):
    r = n1 + n2
    print("%.2f"%(r))
elif(o == '-'):
    r = n1 - n2
    print("%.2f"%(r))
elif(o == '*'):
    r = n1 * n2
    print("%.2f"%(r))
else:
    r = n1 / n2
    print("%.2f"%(r))'''
# 7 - periodo
'''l = input()
l = float(l)
t = 2 * ma.pi * ma.sqrt(l/9.8)
print("%.2f"%(t))'''
#8 - ano bissexto
'''a = input()
a = int(a)
if (a % 4 == 0 or a % 400 == 0):
    print('bissexto')
else:
    print('comum')'''
#9 - norma - manhathan
'''x1, y1, z1 = input(). split()
x2, y2, z2 = input().split()
x1, y1, z1 = float(x1), float(y1), float(z1)
x2, y2, z2 = float(x2), float(y2), float(z2)
if((x1 - x2) < 0):
    dmx = (x1-x2)*(-1)
else: 
    dmx = x1 - x1
if((y1 - y2) < 0):
    dmy = (y1 - y2)*(-1)
else:
    dmy = y1 - y2
if((z1 - z2) < 0):
    dmz = (z1 - z2)*(-1)
else:
    dmz = z1 - z2
dmf = dmx + dmy + dmz
de = ma.sqrt(((x1 - x2)**2)+((y1 - y2)**2)+((z1 - z2)**2))
print('%.2f'%dmf,' %.2f'%de)'''
#10 - triangulo retangulo
'''ab = input()
bc = input()
ab, bc = float(ab), float(bc)
a = ma.atan(ab/bc)
r = int(round(ma.degrees(a)))
print(r)'''

   





