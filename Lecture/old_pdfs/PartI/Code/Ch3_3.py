# --- Pythagorean Positive Integers
c = int(input('Enter an integer: '))

a = 0
while c - a > 0:
    b = 0
    while c - b > 0:
        if a**2 + b**2 == c:
            print('-----')
            print('A=',a)
            print('B=',b)
        b = b + 1
    a = a + 1


# --- Simple String Example

for letter in "Pumpkin Pie":
    print(letter)

dessert = "Pumpkin Pie"
i = 0
while i < len(dessert):
    print(dessert[i])
    i = i + 1


# --- For Ranging Examples
for n in range(5):
    print(n)

for n in range(1,11):
    print(n)

for n in range(10,0,-1):
    print(n)

# --- For loop version of Pythagorean Integers
for a in range(250):
    for b in range(250):
        if a**2 + b**2 == 250:
            print('-----')
            print('A=', a)
            print('B=', b)

# --- Checking Vowels
s = input('Enter a sentence: ')

count = 0
for c in s:
    if c in 'aeiou':
        count = count + 1
print('Number of vowels:',count)

# --- Summing string decimal numbers
s = input('Enter a string of decimal numbers'
        ' separated by commas: ')

curr_num = ''
running_total = 0
for c in s:
    if c == ',':
        running_total = running_total + float(curr_num)
        curr_num = ''
    else:
        curr_num = curr_num + c
running_total = running_total + float(curr_num)
print(running_total)


