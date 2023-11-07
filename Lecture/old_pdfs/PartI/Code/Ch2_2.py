# Conditional Syntax
A = True
B = 10
C = 5 == B

if A:
    print('The test is true!')
else:
    print('The test is false!')



# Elif statements Traffic lights type out
light_color = ____

if light_color == 'Green':
    print('Keep going!')
elif light_color == 'Yellow':
    print('Slow down!')
elif light_color == 'Red':
    print('Stop!!')
else:
    print('What country are you in?!')

## version 2
light_color = ____
time_since_changed = ____ #seconds

if light_color == 'Green':
    print('Keep going!')
elif light_color == 'Yellow':
    if time_since_changed < 2:
        print('Gun it!')
    else:
        print('Slow down!')
elif light_color == 'Red':
    print('Stop!!')
else:
    print('What country are you in?!')


## Understanding Check
animal = 'goat'
number = 3

if animal == 'kitten':
    if number > 10:
        print('I am in heaven!')
    else:
        print('I am still happy!')
elif animal == 'goat' and number > 5:
    print('This is getting excessive.')
elif animal == 'shark':
    if number == 0:
        print('I am ok with this.')
    else:
        print('This is the worst day.')
else:
    if number == 0:
        print('I am lonely')
    else:
        print('Today is an ok day.')


# Stringy Operations
'ape' < 'tuberculosis'
'ape' < 'Tuberculosis'
'ape' < 'tUBERCULOSIS'


# Input Examples
name = input('What is your name? ')
year = int(input('In what year were you born? '))

age = 2019 - year
print("Your name is " + name + " and you are " + str(age) + " years old.")


