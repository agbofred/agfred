def rev_q():
    A = '{:<12,f} & {:0>4d}'.format(1.01234984E5, 320//8)
    B = '{:>12,.2f} & {:0>4d}'.format(1.01234984E5, 32000//8)
    C = '{:<12,.2f} & {:<4d}'.format(1.01234984E5, 3200//8)
    D = '{:<12,.2f} & {:0<4d}'.format(1.01234984E5, 32//8)
    for s in [A,B,C,D]:
        print(s)


def fstr_examples():
    A = 10
    B = 3.15234
    print(f'{A:.0e} is not equal to {B:<10.3f}.')


def class_starts():
    class Person:
        pass

    A = Person()
    B = Person
    print(type(A))
    print(type(B))


if __name__ == '__main__':
    # rev_q()
    fstr_examples()
