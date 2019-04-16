import re

print('''
~ - negation
& - conjunction
| - disjunction
=> - implication
<=> - equivalence

Do not write proposition in lowercase letters!
Do not put spaces!
This program is case sensitive!

''')

S = input()

pattern = re.compile('[A-Z()=><~&|]')
Lo = pattern.findall(S)
assert len(Lo) == len(S), 'Unaccepted symbols in the expression'


def check_formula(L):
    for i in range(len(L)-1, -1, -1):
        if L[i] == '(':
            if L[i+1] == '~':
                assert L[i + 2].isalpha() == True, f'A proposition is expected after negation on position {i+2}'
                assert L[i+3] == ')', f'An ending paranthesis is expected on position {i+3}'
                L[i] = 'P'
                for x in range(3):
                    L.pop(i+1)
                print(''.join(L))
            else:
                assert L[i+1].isalpha() == True, f'A proposition is expected on position {i+1}'
                assert L[i+2] == '&' or L[i+2] == '|' or L[i+2] == '=' or L[i+2] == '<', f'Logical connector expected after proposition on position {i+2}'
                if L[i+2] == '&' or L[i+2] == '|':
                    assert L[i+3].isalpha() == True, f'A proposition expected after a logical connector on position {i+3}'
                    assert L[i+4] == ')', f'An ending paranthesis expected on position {i+4}'
                    L[i] = "P"
                    for x in range(4):
                        L.pop(i+1)
                    print(''.join(L))
                elif L[i+2] == '=':
                    assert L[i+3] == '>', f'Unaccepted logical connector on position {i+2}'
                    assert L[i+4].isalpha() == True, f'Proposition expected after implication on position {i+4}'
                    assert L[i+5] == ')', f'An ending paranthesis expected on position {i+5}'
                    L[i] = 'P'
                    for x in range(5):
                        L.pop(i+1)
                    print(''.join(L))
                elif L[i+2] == '<':
                    assert L[i+3] == '=', f'Unaccepted logical connector on position {i+2}'
                    assert L[i+4] == '>', f'Unaccepted logical connector on position {i+2}'
                    assert L[i+5].isalpha() == True, f'Proposition expected after equivalence on position {i+5}'
                    assert L[i+6] == ')', f'An ending paranthesis expected on position {i+6}'
                    L[i] = 'P'
                    for x in range(6):
                        L.pop(i+1)
                    print(''.join(L))


check_formula(Lo)


print(S, 'is indeed a well formed formula of propositional logic')
