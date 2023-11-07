# --- Review Question
def rev_q():
    def rec(s):
        if len(s) <= 1:
            return s.upper()
        elif s[-2] == ' ':
            return rec(s[:-2]) + s[-1].upper()
        else:
            return rec(s[:-1]) + s[-1]
        
    print(rec('My name is ABE'))


def write_sin():
    import math

    # Amplitude of 20
    def wave(x):
        return int(20 * math.sin(x/5) + 20)

    def line(x):
        dot_index = wave(x)
        pre = '-'*dot_index
        # post = ' '*(40-dot_index)
        return pre + 'o'# + post

    f = open('Sine.txt', 'w')
    for x in range(200):
        f.write(line(x) + '\n')
    f.close()


def read_class():
    import random

    def cut(name):
        middle = len(name)//2
        return name[:middle], name[middle:]

    def combine(name1, name2):
        n1_1, n1_2 = cut(name1)
        n2_1, n2_2 = cut(name2)
        return n1_1 + n2_2, n2_1 + n1_2

    def get_names():
        id1 = random.randint(0,21)
        id2 = random.randint(0,21)

        f = open('Class.txt', 'r')
        l = 0
        for line in f:
            if l == id1:
                name1 = line.strip()
            if l == id2:
                name2 = line.strip()
            l += 1
        return name1, name2

    n1, n2 = get_names()
    print(combine(n1, n2))


def append_wttr():
    def add_line(temp, hum):
        f = open('Weather.txt', 'a')
        f.write('Temp: '+ temp +  '  Humidity: '+ hum + '\n')
        f.close()

    temp = '50'
    while temp:
        temp = input('Enter the temperature: ')
        hum = input('Enter the humidity: ')
        print('-'*20)
        add_line(temp, hum)


def odd_sum(maxnum=10):
    global total
    def add_odd(x):
        global total
        if x % 2 == 1:
            total += x

    total = 0
    for n in range(maxnum+1):
        add_odd(n)
    return total

def rec_arcade():
    import arcade
    import math

    def main():
        SIZE = 800
        arcade.open_window(SIZE, SIZE, 'Test')
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        rec_tri(0,0,SIZE)
        arcade.finish_render()
        arcade.run()

    def rec_tri(x,y,L):
        if L > 5:
            p2x = x + L
            p2y = y
            p3x = x + math.cos(60*math.pi/180)*L
            p3y = y + math.sin(60*math.pi/180)*L
            arcade.draw_triangle_outline(x,y,p2x,p2y,p3x,p3y,arcade.color.GREEN)

            midx1 = x + L/2
            midy1 = y
            midx2 = x + math.cos(60*math.pi/180)*L/2
            midy2 = y + math.sin(60*math.pi/180)*L/2
            rec_tri(x,y,L/2)
            rec_tri(midx1, midy1, L/2)
            rec_tri(midx2, midy2, L/2)

    main()

if __name__ == '__main__':
    # rev_q()
    # write_sin()
    # read_class()
    # append_wttr()
    # print(odd_sum())
    rec_arcade()
