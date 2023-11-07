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

    A = ['tuna']
    A.append(['Cod', 'Halibut', 'Salmon'])
    print(A)


# ---  Cloning Fixes
def clones1():
    A = ['Aardvark', 'Butterfly', 'Centipede']
    B = A[:]

    B.append('Deer')
    B.remove('Butterfly')

    print(A)
    print(B)

def clones2():
    A = [1,2,3,4,5,6,7,8,9]

    for i,num in enumerate(list(A)):
        print('At index:', i)
        if 3 < num < 6:
            A.remove(num)

    print(A)


def UCheck():
    A = ['Fox', 'Giraffe', 'Hippo']
    A.append('Iguana')
    A[:].reverse()
    B = A
    for anim in B:
        if anim[1] == 'i':
            B.remove(anim)

    print(A)


def list_cmp():
    L = [x**2 for x in range(10)]
    print(L)

    L2 = [x**2 for x in range(10) if x > 5]
    print(L2)

    # Probably shouldn't overburden with this one
    L3 = [x**2 if x > 5 else x for x in range(10)]
    print(L3)

    L4 = ['fish', 3, 'sword', 9, 58, 3.14159, True, False]
    filt = [x for x in L4 if type(x) == int]
    print(filt)










if __name__ == '__main__':
    # lst_ex()
    # clones1()
    # clones2()
    # UCheck()
    list_cmp()
