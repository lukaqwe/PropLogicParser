def neg(A):
    C = [0]*len(A)
    for i in range(len(A)):
        if A[i] == '0':
            C[i] = '1'
    return C


def impl(A, B):
    return disj(neg(A), B)


def conj(A, B):
    C = []
    for i in range(len(A)):
        C.append(bin(int(A[i]) & int(B[i]))[-1])
    return C


def disj(A, B):
    C = []
    for i in range(len(A)):
        C.append(bin(int(A[i]) | int(B[i]))[-1])
    return C


def equi(A, B):
    return conj(impl(A, B), impl(B, A))
