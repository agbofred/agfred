# ------ Lost Woods Simple Example -------
d = None
while d != 'L':
    print('')
    print('*'*32)
    print('*'*32)
    print(' '*15 + ':)' + ' '*15)
    print('*'*32)
    print('*'*32)
    d = input('Go (L)eft or (R)ight? ')

print('You escaped!')

# ------ Lost Woods Middle Example -------
d = None
counter = 0
while d != 'L':
    print('')
    print('*'*24)
    print('*'*24)
    if counter > 10:
        man = 'D:'
    elif counter > 5:
        man = ':('
    else:
        man = ':)'
    print(' '*12 + man + ' '*12)
    print('*'*24)
    print('*'*24)
    d = input('Go (L)eft or (R)ight? ')
    counter = counter + 1

print('You escaped!')

# ------ Lost Woods Complex Example -------
dir = 'W'
onpath = 0
atEnd = False
while not atEnd:
    print('')
    print('*'*10 + '     ' + '*'*10)
    print('*'*10 + '     ' + '*'*10)
    print(' '*10 + ' :) ' + ' '*10)
    print('*'*10 + '     ' + '*'*10)
    print('*'*10 + '     ' + '*'*10)
    dir = input('Go (N)orth, (S)outh, (E)ast, or (W)est? ')

    if dir == 'N' and onpath == 0:
        onpath = 1
    elif dir == 'W' and onpath == 1:
        onpath = 2
    elif dir == 'S' and onpath == 2:
        onpath = 3
    elif dir == 'W' and onpath == 3:
        atEnd = True
    else:
        onpath = 0

print('You escaped!')



# Dual Loops Example
num1 = 1
while num1 <= 9:
    row = ''
    num2 = 1
    while num2 <= 9:
        product = str(num1*num2)
        if len(product) == 1:
            product = ' ' + product
        row = row + ' ' + product
        num2 = num2 + 1
    print(row)
    num1 = num1 + 1



# Break Example
num1 = 1
while num1 <= 9:
    row = ''
    num2 = 1
    while num2 <= 9:
        product = str(num1*num2)
        if len(product) == 1:
            product = ' ' + product
        row = row + ' ' + product
        num2 = num2 + 1
        if num2 > num1:
            break
    print(row)
    num1 = num1 + 1


# Understanding Check
x = 1
while x < 10:
    y = 10
    while y > x:
        if y % 3 == 0:
            break
        print(x*y)
        y = y - 2
    x = x + 1

# Indexing Strings
x = 'Spaghetti'
print(x[0] + x[1] + x[2])
print(x[1] + x[-1] + x[3])
print(x[4:-2])
print(x[:-2])
print(x[::2])
print(x[::-2])
print(x[-2:0:-3])
