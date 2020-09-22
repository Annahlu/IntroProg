# -*- coding: utf-8 -*-
import numpy as np
import math as math
"""
Created on Thu Sep 17 22:46:44 2020

@author: analu
"""
#1
'''def reverse(x): 
  str = "" 
  for i in x: 
    str = i + str
  return str
x = input()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(reverse(x))'''
#3
'''e = input()
f,e = e.split('=')
print("e" +e)
print("f" +f)
f = f.replace('y','x')
e = e.replace('x','y')
print(""+ f + "=" + e)'''
#4
'''a = input()
b = input()
x1,y1,z1 = a.split()
x2,y2,z2 = b.split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
z1 = float(z1)
z2 = float(z2)
y1 = float(y1)
z1 = float(z1)
x2 = float(x2)
y2 = float(y2)
z2 = float(z2)
c=np.array([x1,y1,z1])
d=np.array([x2,y2,z2])
rx = x1+x2
ry = y1+y2
rz = z1+z2
pe = np.dot(c,d)
x, y, z =np.cross(c,d)
print('.2f'%rx,' .2f'%ry, '%.2f'%rz)
print("%.2f"%(pe))
print('.2f'%x,' .2f'%y, '%.2f'%z)'''
#5 
'''f = input()
fa = float(f)
c = (5/9)*(fa-32)
print("%.2f"%(c))'''
#6
'''n = input()
qtd = float(input())
vu = float(input())
d = float(input())
de = qtd*vu*(d/100)
pr = (qtd*vu)-de
print(""+ n +": R$ %.2f"%(pr)) '''
#7
'''i = input()
h,m,s = i.split(":")
h = int(h)
m = int(m)
s = int(s)
t = (h*3600)+(m*60)+s
print(t)'''
#8
'''t = input()
t = float(t)
x = (t*340)/1000
print("%.2f"%(x))'''
#9
'''x = input()
a, t = x.split()
a = float(a)
t = float(t)
d = (t**2)*a/2
print("%.2f"%(d))'''
#10
'''e = input()
v, x = e.split()
v = float(v)
x = float(x)
a = (v*v)/(2*x)
tq = (2*x)/a
t = math.sqrt(tq)
print("%.2f" %a " .2f"%t)'''




