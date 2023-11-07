# --- Basic Example
def Basic_Example():
    guess = 1
    epsilon = 0.01
    while abs(8*guess**2 - 3) > epsilon:
        val = 8*guess**2 - 3
        deriv = 16*guess
        guess -= val / deriv
    print(guess)

# --- Cube root of 27 with Newton
def CubeRootNewton():
    guess = 1
    epsilon = 0.01
    num_guess = 1
    while abs(guess**3 - 27) > epsilon:
        val = guess**3 - 27
        deriv = 3*guess**2
        guess -= val/deriv
        num_guess += 1
    print('Solution:',guess)
    print('Took', num_guess, 'guesses.')



# --- Multiroot Example
def Multiroot():
    g = float(input('Enter a guess for a solution: '))
    epsilon = 0.1
    f = (g+3)**3 + 5*g**2 - 15*g - 200
    while abs(f - 0) > epsilon:
        num = (g+3)**3 + 5*g**2 - 15*g - 200
        deriv = 3*(g+3)**2 + 10*g - 15
        g -= num/deriv
        f = (g+3)**3 + 5*g**2 - 15*g - 200
    print('Solution:', g)


if __name__ == '__main__':
    # Basic_Example()
    # CubeRootNewton()
    Multiroot()

