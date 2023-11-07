import arcade

WIDTH = 300
HEIGHT = 300
arcade.open_window(WIDTH, HEIGHT, 'Review Question')

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

i = 0
while i < WIDTH:
    A = i / WIDTH * 360
    arcade.draw_arc_outline(i, 150, 20, 20, arcade.color.BLACK, A, A+90, 15)
    i = i + 30

arcade.finish_render()

arcade.run()


# # ------- While Loops and Slicing
# x = 'Metamorphasis'

# i = 4
# piece = ""
# while i < 9:
    # piece = piece + x[i]
    # i = i + 1
# print(piece)

# print(x[4:9])


# # ---------- Dicing Examples
# x = 'Metamorphasis'

# print(x[0:6:2])
# print(x[::-1])


# ----------  Guess and Check our Problem
# x = 0
# while x <= 36:
    # if (x + 12)**2 == 36:
        # print('An answer is:', x)
    # if (-x + 12)**2 == 36:
        # print('An answer is:', -x)

    # x = x + 1

# # This is clunky and probably not worth discussing
# x = -18
# while 36 - (x + 12)**2 > 0:
    # print(36 - (x+12)**2)
    # x = x + 1
# print('An answer is:',x)



# # ------------ Modern Speed
# import time

# maxVal = int(input("Enter a positive integer: "))
# start = time.time()
# i = 0
# while i < maxVal:
    # i = i + 1
# print(i)
# end = time.time()
# print('Operation took:', end-start, 'seconds.')



# ---------- Exhaustive letters

# import random

# letters = 'abcdefghijklmnopqrstuvwxyz'

# secret_letter = random.choice(letters)

# i = 0
# while letters[i] != secret_letter:
    # i = i + 1
# print('Found the secret letter to be:', letters[i])
# print('Secret letter actually was:', secret_letter)

