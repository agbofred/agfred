import pandas as pd

def exh_enum(target):
    diffs = []
    for x in range(101):
        diffs.append(target-x)
        if x == target:
            break
    return diffs

def bisection_search(target):
    diffs = []
    low = 0
    high = 101
    x = (low + high) // 2
    while x != target:
        diffs.append(target-x)
        if x > target:
            high = x
        elif x < target:
            low = x
        x = (low + high) // 2
    return diffs

def root_bisect(val):
    low = 0
    high = val
    guess = (low + high) / 2
    epsilon = 0.01
    diffs = []
    while abs(guess**3 - val) > epsilon:
        if guess**3 > val:
            high = guess
        else:
            low = guess
        diffs.append(guess**3 - val)
        guess = (low + high) / 2
    return diffs

def root_Newton(val):
    guess = val/2
    epsilon = 0.01
    diffs = []
    while abs(guess**3 - val) > epsilon:
        diffs.append(guess**3-val)
        num = guess**3 - val
        deriv = 3*guess**2
        guess -= num/deriv
    return diffs




if __name__ == '__main__':
    val = 15
    df = pd.DataFrame.from_dict({'Exh':exh_enum(val), 'Bis':bisection_search(val)}, orient='index')
    df = df.transpose().fillna(0)
    df.index.name = 'Iter'
    df.to_csv('Convergence.csv')

    cuberootof = 27
    df = pd.DataFrame.from_dict({'Bis':root_bisect(cuberootof), 'Newt':root_Newton(cuberootof)}, orient='index')
    df = df.transpose().fillna(0)
    df.index.name = 'Iter'
    df.to_csv('Convergence2.csv')

