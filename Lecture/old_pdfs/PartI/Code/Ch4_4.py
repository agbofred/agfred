
def fib(n):
    print('Running fib!')
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def rec_str_rev(s):
    if len(s) == 1:
        return s
    else:
        return rec_str_rev(s[1:]) + s[0]


def prune_dupes(s):
    if len(s) == 1:
        return s
    elif s[0] == s[1]:
        print('Dropping the letter:', s[0])
        return prune_dupes(s[1:])
    else:
        return s[0] + prune_dupes(s[1:])

def file_write():
    fhandle = open('Names.txt', 'w')
    for i in range(3):
        name = input('Enter a name: ')
        fhandle.write(name + '\n')
    fhandle.close()

def file_read():
    f = open('Names.txt', 'r')
    for line in f:
        # print(repr(line))
        if line.strip() == 'Betty':
            print('This is Betty!')
        else:
            print('This is not Betty!')
    f.close()

if __name__ == '__main__':
    # print('The fifth fibonacci number is', fib(5))
    # print(rec_str_rev("hi there!"))
    print(prune_dupes('aaallllrighty then'))
    
