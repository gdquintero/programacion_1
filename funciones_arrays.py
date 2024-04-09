import numpy as np

def par_impar(n):
    if n % 2 == 0:
        msg = "El numero es par"
    else:
        msg = "El numero es impar"

    return msg

par_impar(90)

def f(x):
    return np.exp(np.sin(x))-2

def g(x):
    return np.cos(x) * np.exp(np.sin(x))

def punto_medio(a,b):
    return (a + b) / 2

def bolzano(a,b):
    p = punto_medio(a,b)
    tol = 1e-8
    max_iter = 1000
    iter = 0

    while iter <= max_iter and abs(f(p)) > tol:
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p

        p = punto_medio(a,b)
        iter += 1

    return p,f(p),iter

def newton(a,b):
    tol = 1e-8
    max_iter = 1000
    iter = 0

    x = -3

    while iter <= max_iter and abs(f(x)) > tol:
        x = x - f(x)/g(x)
        iter += 1

    return x,f(x),iter

def secante(a,b):
    tol = 1e-8
    max_iter = 1000
    iter = 0

    xn = -3
    xn_1 = -4.5

    while iter <= max_iter and abs(f(xn)) > tol:
        xn = xn_1 - f(xn_1) * (xn_1 - xn) / (f(xn_1) - f(xn))
        iter += 1

    return xn,f(xn),iter

print(bolzano(-5,-3))
print(newton(-5,-3))
print(secante(-5,-3))

def poly(a0,a1,a2,a3,x=0):
    return a0 + a1 * x + a2 * x**2 + a3 * x**3

x = np.ones(4)
print(poly(*x))

def producto_interno(x,y,n):
    suma = 0

    for i in range(n):
        suma += x[i] * y[i]

    return suma

def producto_escalar_vector(a,x):
    for i in range(len(x)):
        x[i] = a * x[i]

    return x

def producto_externo(x,y):
    m = len(x)
    n = len(y)

    A = np.zeros((m,n))

    for i in range(m):
        for j in range(n):
            A[i,j] = x[i] * y[j]


    return A


v = [2,3,4,1,2]

x = np.zeros(10)
x = np.empty(10)
x = np.array([1,2])
y = np.array([3,2,1])

producto_externo(x,y)

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],dtype=int)

print(A)