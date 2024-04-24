import numpy as np
import scipy as sc

def solve_with_lu(A,b,n):
    P, L, U = sc.linalg.lu(A)

    y = np.linalg.solve(L,b)
    x = np.linalg.solve(U,y)

    return x

A = np.array([
    [3,2,1,4],
    [-2,1,4,2],
    [6,2,-1,-2],
    [0,2,1,3]])

b = np.ones(4)

x = solve_with_lu(A,b,4)

B = np.loadtxt("inferior.txt")

print(B[:,0])



