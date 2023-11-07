# # --- Guessing Game Algorithm
# my_value = int(input('Enter the number to guess: '))

# low = 0
# high = 101

# guess = None
# guess_count = 0

# while guess != my_value:
    # guess = (low+high)//2
    # guess_count += 1
    # print('I am guessing:', guess)
    # if guess > my_value:
        # print('It was too high!')
        # high = guess
    # elif guess < my_value:
        # print('It was too low!')
        # low = guess
    # else:
        # print('I guessed it!')
# print('It took me', guess_count, 'guesses!')

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

# # --- Multiplying Rabbits
# goal = 1000
# epsilon = 2
# low = 0
# high = 1
# guess = (low + high) / 2

# n_rabbits = 10
# while abs(n_rabbits - goal) > epsilon:
    # n_rabbits = 10
    # death_perc = guess
    # for year in range(10):
        # # n_rabbits += ((1-death_perc)*n_rabbits)//2 * 4 - int(n_rabbits * death_perc)
        # n_rabbits += (n_rabbits)//2 * 4 - int(n_rabbits * death_perc)
    # print('Guessed', guess)
    # print('Rabbits alive:', n_rabbits)

    # if n_rabbits > goal:
        # low = guess
    # elif n_rabbits < goal:
        # high = guess
    # guess = (low + high) / 2
# print('Death percentage:', guess)


# # --- Intersection of Two Lines
# A = float(input('Enter A: '))
# B = float(input('Enter B: '))
# C = float(input('Enter C: '))
# D = float(input('Enter D: '))

# epsilon = 0.01
# num_guess = 0
# low = 0
# high = 10
# x = (low+high)/2

# y1 = A*x+B
# y2 = C*x+D

# while abs(y1-y2) > epsilon and num_guess < 1000:
    # if A > C: #Checking which slope is larger
        # if y1 > y2:
            # high = x
        # else:
            # low = x
    # else:
        # if y2 > y1:
            # high = x
        # else:
            # low = x

    # x = (low + high)/2
    # y1 = A*x+B
    # y2 = C*x+D
    # num_guess += 1

# print('Took', num_guess, 'guesses')
# if abs(y1-y2) < epsilon:
    # print(x,y1)
# else:
    # print('No solution found')


# import matplotlib.pyplot as plt
# import numpy as np

# xs = np.arange(0,10,0.01)
# plt.plot( xs, A*xs+B, label='y1')
# plt.plot( xs, C*xs+D, label='y2' )
# plt.plot([x,x],[y1,y2], '.r', markersize=20)
# plt.legend()
# plt.show()
