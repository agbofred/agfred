
# ---  Review Question
def rev_q():
    A = ('pirate', 'ninja')
    B = ('samurai',) + A
    C = (B, ('ship', 'rope', 'horse'))
    D = C[::-1]

    print('a) ', D[1][0])
    print('b) ', D[0][1])
    print('c) ', D[0][2])
    print('d) ', D[1][2])

    return D

# ---  Multiple Assignment
def mult_assign():
    x, y, z = ('fish', 'steak', 'potatoes')

    print('x is', x)
    print('y is', y)
    print('z is', z)


# ---  Enumerate Example
def enum():
    t = ('fish', 'steak', 'potatoes')
    for i, v in enumerate(t):
        print('The index is:', i, 'and the element is:', v)


# ---  Lists Example
def lst_ex():
    A = ['tuna']
    A.append('Cod')
    A.append('Halibut')
    A.append('Salmon')
    print(A)

    A = ['tuna']
    A.extend(['Cod', 'Halibut', 'Salmon'])
    print(A)











if __name__ == '__main__':
    # rev_q()
    # mult_assign()
    # enum()
    lst_ex()
