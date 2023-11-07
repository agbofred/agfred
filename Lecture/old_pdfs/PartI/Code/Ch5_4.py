def rev_q():
    A = [i*j for i,j in enumerate(['c','o','w'])]
    print(A[2])

def list_cmp():
    L = [x**2 for x in range(10)]
    print(L)

    L2 = [x**2 for x in range(10) if x > 5]
    print(L2)

    L4 = ['fish', 3, 'sword', 9, 58, 3.14159, True, False]
    filt = [x for x in L4 if type(x) == int]
    print(filt)

def lst_cmp_counting():
    import random
    A = [random.random() for _ in range(1000)]

    T = 0
    for x in A:
        if x > 0.5:
            T += 1
    print(T)

    T = sum([1 for x in A if x > 0.5])
    print(T)

    T = sum([1 if x > 0.5 else 0 for x in A])
    print(T)


def funcs_in_lists():
    def f1(x):
        return x**2

    def f2(x):
        return x // 2

    def f3(x):
        if x > 0.5:
            return 1
        else:
            return 0

    L = [f1,f2,f3]
    A = [1,2,3,4,5]
    for num in A:
        print('Number:',num)
        for f in L:
            print(f(num))


def funcs_to_lists():
    def apply_func_2_list(func, list_):
        L = []
        for value in list_:
            L.append(func(value))
        return L

    def f(x):
        return x**3

    def fib(x):
        if x==1 or x==2:
            return 1
        else:
            return fib(x-1) + fib(x-2)

    A = [1,2,3,4,5]
    print(apply_func_2_list(f,A))

    B = [1,3,5,7,9]
    print(apply_func_2_list(fib,B))

def mapping_example():
    def g(x):
        return 4*x + 2
    xs = [1,2,3,4,5,6]
    for res in map(g,xs):
        print(res)


def multi_mapping_example():
    def h(x,y):
        return 4*x + 2 * y

    xs = [1,2,3,4,5,6]
    ys = xs[::-1]
    hs = [res for res in map(h,xs,ys)]
    print(hs)


def multi_lambda_funcs():
    xs = range(1,7)
    ys = [r for r in map(lambda x,y: 4*x + 2*y, xs, xs[::-1])]
    print(ys)












if __name__ == '__main__':
    # rev_q()
    # list_cmp()
    # lst_cmp_counting()
    # funcs_in_lists()
    # funcs_to_lists()
    # mapping_example()
    multi_mapping_example()
    multi_lambda_funcs()
