# --- 3 digit prime
n = int(input('Enter a number to check if prime: '))

x = 2
while n - x > 0 and n % x != 0:
    x = x + 1
if x == n:
    print('Number is prime!')
else:
    print('Number is evenly divisible by', x)

# --- or

n = int(input('Enter a number to check if prime: '))

x = 2
is_prime = True
while n - x > 0:
    if n % x == 0:
        is_prime = False
        print('Number is divisible by', x)
        break
    x = x + 1
if is_prime:
    print('Number is prime!')


# --- Finding Substrings?

b_str = 'This is a great and glorious sentence.'
l_str = input('Enter the desired substring to search for: ')

i = 0
found_str = False
while len(b_str) - len(l_str) - i + 1 > 0:
    if b_str[i:i+len(l_str)] == l_str:
        print('Substring found starting at index:', i)
        found_str = True
        break
    i = i + 1

if not found_str:
    print('Substring not found in larger string')



# --- Money Money!

max_nic = 3
max_dime = 2
max_pen = 8

val_nic = 5
val_dime = 10
val_pen = 1

num_nic = 0
while num_nic <= max_nic:
    num_dime = 0
    while num_dime <= max_dime:
        num_pen = 0
        while num_pen <= max_pen:
            total = (val_nic * num_nic + 
                    val_dime * num_dime +
                    val_pen * num_pen )
            if total == 25:
                print(num_nic, 'nickels', 
                        num_dime, 'dimes, and', 
                        num_pen, 'pennies')
            num_pen = num_pen + 1
        num_dime = num_dime + 1
    num_nic = num_nic + 1


# --- Pythagorean Positive Integers
c = int(input('Enter an integer: '))

a = 0
# while a**2 <= c:
while c - a > 0:
    b = 0
    # while b**2 <= c - a**2:
    while c - b > 0:
        if a**2 + b**2 == c:
            print('-----')
            print('A=',a)
            print('B=',b)
        b = b + 1
    a = a + 1


# --- Simple String Example

# for letter in "Pumpkin Pie":
    # print(letter)

# dessert = "Pumpkin Pie"
# i = 0
# while i < len(dessert):
    # print(dessert[i])
    # i = i + 1


# --- For Ranging Examples
for n in range(5):
    print(n)

for n in range(1,11):
    print(n)

for n in range(10,0,-1):
    print(n)
