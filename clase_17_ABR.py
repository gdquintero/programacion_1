import numpy as np

def transpuesta(A,T,m,n):
    # for i in range(n):
    #     for j in range(m):
    #         T[i,j] = A[j,i]

    for i in range(m):
        T[:,i] = A[i,:]

    return T

f = lambda x : 2*x + 1

# print(f(2))

A = np.array([[1,5,6,3,8],
              [4,2,1,6,8],
              [4,1,6,3,2]])

m, n = np.shape(A)

T = np.empty((n,m))

print(transpuesta(A,T,m,n))





