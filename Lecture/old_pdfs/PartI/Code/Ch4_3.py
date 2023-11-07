# --- Review Question
def rev_quest():
    def func(a, b=5, c=True):
        if c:
            return a + b
        else:
            return a * b

    print(func(10,False))


# --- Looping Example
def mult_w_loop(A,B):
    total = 0
    for i in range(B):
        total += A
    return total

def mult_w_rec(A,B):
    if B == 1:
        return A
    else:
        return A + mult_w_rec(A,B-1)


# --- Factorial Example
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
