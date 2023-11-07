
## --- Main Name Example

# pi = 3.14159

# def area(radius):
    # return pi * radius**2


# print('The area is', area(4))

# --- Tuple Assigning
def tuple_assign():
    t_one = (1,2,3,4,5)
    t_three = (1, 'a', 2, 'fish', True)

    print(t_one)
    print(type(t_one))

    print(t_three)
    print(type(t_three))


def tuple_ops():
    t_one = (1,2,3,4)
    t_two = ('a', 'b', 'c', 'd')

    print(t_one + t_two)
    print(3*t_two)
    print(t_one[0])
    print(t_two[:-2])
    # print(t_one[0] + t_two[0])


def nested_tuples():
    t1 = (1,2,3)
    t2 = ('a','b','c')
    t3 = (t1,t2)

    print(t3[1][0])


def under_check():
    A = (1,3,5)
    B = (2*A, ('a',))
    C = B + ('b','c','d')
    D = ()
    for v in C[:2]:
        D += v[:1]
    print(D)
