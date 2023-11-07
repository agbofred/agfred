
# --- Review code
def rev_code():
    def func(A):
        m = str(A)
        n = m * 10
        print(n)

    y = 5.0
    x = func(y)
    print(type(x))

# --- Opinion Poll
def op_poll():
    def vegas(x):
        y = 2
        for i in range(5):
            x = x + y
        return x

    x = 3
    z = vegas(x)
    print('z =', z)
    print('x =', x)

# --- Scoping Demo
def scope_demo():
    def f():
        # def h():
            # print(x)
        # h()
        print(x)
        # z = x + 1
        # print(z)

    x = 2
    f()

def anim_demo():
    import arcade
    import colorsys

    # Add after discussing scope
    WIDTH=1900
    HEIGHT=1080

    def main():
        global bx,by,dx,dy
        bx, by = WIDTH/2, HEIGHT/2
        dx, dy = 2, 2
        arcade.open_window(WIDTH,HEIGHT, 'Anim Testing')
        arcade.set_background_color(arcade.color.BLUE_BELL)
        arcade.start_render()
        arcade.schedule(on_draw, 1/120)
        arcade.run()

    def draw_happy_box(x,y,hue):
        rgb = [int(255*x) for x in colorsys.hsv_to_rgb(hue, 1, 1)]
        arcade.draw_rectangle_filled(x,y, 50, 50, rgb)
        arcade.draw_circle_filled(x+7,y+7, 3, arcade.color.BLACK)
        arcade.draw_circle_filled(x-7,y+7, 3, arcade.color.BLACK)
        arcade.draw_arc_filled(x, y, 20,10, arcade.color.BLACK, 180, 360)

    def on_draw(dt):
        global bx, by, dx, dy # <-- add after discussing globals
        # arcade.start_render()
        draw_happy_box(bx,by,bx/WIDTH*by/HEIGHT)
        bx += dx
        by += dy
        if bx + 25 > WIDTH or bx-25 < 0:
            dx *= -1
        if by + 25 > HEIGHT or by-25 < 0:
            dy *= -1


    main()




if __name__ == '__main__':
    # rev_code()
    # op_poll()
    # scope_demo()
    anim_demo()
