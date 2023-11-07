# --- Varied Examples
def print_stuff():
    print("Stuff 1")
    print("Stuff 2")


def print_mult_of_A(A):
    print(A, 2 * A, 3 * A, 4 * A, 5 * A)


def calc_year_savings(init_amt):
    for i in range(12):
        init_amt += init_amt * 0.03 / 12
    return init_amt


# --- Flow Example
def flow_example():
    def year_savings(init_amt, int_rate):
        for i in range(12):
            init_amt *= 1 + int_rate / 12
        return init_amt

    amount = 100
    rate = 0
    while rate < 1:
        print("Savings:", year_savings(amount, rate))
        rate += 0.05

    print("All done!")


# --- Summing Primes
def sum_primes(num=100):
    def is_prime(num):
        for d in range(2, num):
            if num % d == 0:
                return False
        return True

    for a in range(num):
        for b in range(a):
            if is_prime(a) and is_prime(b) and (a + b == num):
                print(a, "and", b, "are both prime and sum to 100!")


# --- Keyword Examples
def keyword():
    def func(first, second, third):
        print(first, second, third)

    func(1, 2, 3)
    func(2, 6, 4)
    func(third=4, first=2, second=6)
    func(2, third=4, second=6)


# --- Default Examples
def defaults():
    def func(name="Jed", age=34):
        print("My name is", name, "and I am", age)

    func()
    func("Bob", 25)
    func("Larry")
    func(age=68)


def is_proper_divisor(x, n):
    return n % x == 0 and x < n


def perfect_numbers_between(x, y):
    for n in range(x, y + 1):
        total = 0
        for d in range(1, int(n ** 0.5) + 1):
            if n % d == 0 and d < n:
                total += d + (n // d)
        total -= n
        if total == n:
            print(n)


if __name__ == "__main__":
    perfect_numbers_between(1, 100000)
