import numpy as np

def producto_interno(x,y,n):
    suma = 0

    for i in range(n):
        suma += x[i] * y[i]

    return suma

def producto_matriz_vector(A,x,b,m,n):

    for i in range(m):
        b[i] = producto_interno(A[i,:],x,n)
    
    return b

A = np.array([
    [1,2],
    [3,4],
    [5,6]])

x = np.array(
    [1,2]
)

m,n = np.shape(A) 
b = np.zeros(m)

print(producto_matriz_vector(A,x,b,m,n))