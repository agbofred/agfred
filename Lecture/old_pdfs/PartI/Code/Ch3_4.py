# # --- Cube root of 27
# x = 27
# epsilon = 0.1
# guess = 0
# num_guesses = 1

# while abs(guess**3 - x) >= epsilon and guess <= x:
    # guess += epsilon**3
    # num_guesses += 1
# print('Took', num_guesses, 'guesses')
# if abs(guess**3 - x) < epsilon:
    # print(guess, 'is close to the cube root of', x)
# else:
    # print('No solution found for cube root of', x)

# # Play with changing x to 0.125 and it failing
# # Play with changing epsilon to 0.01 and seeing the guesses spike


# # --- Ball Toss Example
# v0 = 1
# yi = 2
# g = 9.8
# y_des = 0

# epsilon = 0.1

# t = 0
# y = yi + v0*t - 0.5*g*t**2
# while abs(y - y_des) > epsilon and y > 0:
    # t += epsilon**2
    # y = yi + v0*t - 0.5*g*t**2
# if abs(y - y_des) < epsilon:
    # print('Time to strike ground:', t)
# else:
    # print('The time step was not small enough.')
    # print('A close enough time was not found.')


# # --- Guessing Game Algorithm
# my_value = int(input('Enter the number to guess: '))

# low = 0
# high = 101

# guess = None

# while guess != my_value:
    # guess = (low+high)//2
    # print('I am guessing:', guess)
    # if guess > my_value:
        # print('It was too high!')
        # high = guess
    # elif guess < my_value:
        # print('It was too low!')
        # low = guess
    # else:
        # print('I guessed it!')

# # --- Cube root of 27 with bisection
# x = 27
# epsilon = 0.1
# num_guesses = 1

# low = 0
# high = x
# guess = (low + high) / 2

# while abs(guess**3 - x) >= epsilon:
    # if guess**3 > x:
        # high = guess
    # else:
        # low = guess
    # guess = (low + high) / 2
    # num_guesses += 1
# print('Took', num_guesses, 'guesses')
# if abs(guess**3 - x) < epsilon:
    # print(guess, 'is close to the cube root of', x)
# else:
    # print('No solution found for cube root of', x)
