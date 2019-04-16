from truth_functions import *
import re
print('''
~ - negation
| - disjunction
& - conjunction
=> - implication
<=> - equivalence

First check that formula is well formed
''')

F = input('Formula := ')
pattern = re.compile('[A-Z<=>()~&|]')
L = pattern.findall(F)
S = set(x for x in L if x.isalpha() == True)
I = [x for x in S]
T = []
for i in range(2**len(S)):
    T.append(bin(i)[2:])

for s in range(len(T)):
    while len(T[s]) != len(T[-1]):
        T[s] = '0'+T[s]


def truth_replace(j):
    l = []
    for s in T:
        l.append(s[j])
    return l


for i in range(len(L)):
    for j in range(len(I)):
        if L[i] == I[j]:
            L[i] = truth_replace(j)



for i in L:
    for i in range(len(L)-1, -1, -1):
        if L[i] == '(':
            if L[i+1] == '~':
                L[i] = neg(L[i+2])
                for x in range(3):
                    L.pop(i+1)
            else:
                if L[i+2] == '|':
                    L[i] = disj(L[i+1], L[i+3])
                    for x in range(4):
                        L.pop(i+1)
                elif L[i+2] == '&':
                    L[i] = conj(L[i+1], L[i+3])
                    for x in range(4):
                        L.pop(i+1)
                elif L[i+2] == '=':
                    L[i] = impl(L[i+1], L[i+4])
                    for x in range(5):
                        L.pop(i+1)
                elif L[i+2] == '<':
                    L[i] = equi(L[i+1], L[i+5])
                    for x in range(6):
                        L.pop(i+1)
