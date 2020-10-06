# 2 - S de 1/n
'''n = int(input())
s = 0.00
for i in range(1,n+1):
    d = i
    d = float(d)
    f = 1.0/d
    if (i % 2 == 0):
        s -= f
    else:
        s += f
print('%.2f'%s)'''
#fibonacci
'''n = input()
n = int(n)
fib, fibn, ant = 0, 1, 0
if(n == 0):
    fib = 0
elif(n == 1 or n == 2):
    fib = 1
else: 
    for i in range (0, n):
        fib = fibn + ant
        fibn = ant
        ant = fib
fib = str(fib)
print(fib)'''
#mdc
'''a, b = input().split()
a, b = int(a), int(b)
a, b= max(a,b), min(a, b)
r = a % b
while r:
    a = b
    b = r
    r = a % b
print('b')'''
#triangular
n = input()
n = int(n)
resp = 'não triangular'
m = int(n**(1/3))
for i in range (1, m+1):
    if i*(i+1)*(i+2) == n:
        resp = 'triangular'
        break
print(resp)


