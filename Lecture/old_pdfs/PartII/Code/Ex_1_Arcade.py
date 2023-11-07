
import arcade
import random

def window_test():
    class MyPicture(arcade.Window):
        def __init__(self, width, height, title):
            arcade.Window.__init__(self, width, height, title)
            arcade.set_background_color(arcade.color.BLUE)
            
            self.width = width
            self.height = height

            self.cx = self.width/2
            self.cy = self.height/2
            self.r = 50

            self.xdir = 1
            self.ydir = 2

            self.color = arcade.color.YELLOW_ORANGE

            arcade.run()

        def on_draw(self):
            arcade.start_render()
            arcade.draw_circle_filled(self.cx, self.cy, self.r, self.color)

        def on_update(self, dt):
            self.cx += self.xdir
            self.cy += self.ydir

            if (self.cx+self.r) > self.width or (self.cx-self.r) < 0:
                self.xdir *= -1
            if (self.cy+self.r) > self.height or (self.cy-self.r) < 0:
                self.ydir *= -1

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.SPACE:
                if self.color == arcade.color.YELLOW_ORANGE:
                    self.color = arcade.color.RED_VIOLET
                else:
                    self.color = arcade.color.YELLOW_ORANGE
            elif symbol == arcade.key.Q:
                    arcade.close_window()

        def on_mouse_press(self, x,y,button, modifier):
            if button == arcade.MOUSE_BUTTON_LEFT:
                arcade.set_background_color(arcade.color.GUPPIE_GREEN)



    MyPicture(500,500,'Hi!')



if __name__ == '__main__':
    window_test()
    # extended()
