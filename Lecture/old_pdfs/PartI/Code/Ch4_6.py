
# --- Global Version of HW4
def odd_sum(maxnum=10):
    global total
    def add_odd(x):
        global total
        if x % 2 == 1:
            total += x

    total = 0
    for n in range(maxnum+1):
        add_odd(n)
    return total


# --- More Global Play
def global_play():
    global X #<- don't include when doing in main scope
    X = 10

    def update_X():
        global X
        X += 1

    for i in range(5):
        update_X()

    print(X)

if __name__ == '__main__':
    pass
    # print(odd_sum())
    global_play()
