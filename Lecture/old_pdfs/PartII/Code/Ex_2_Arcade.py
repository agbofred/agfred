import arcade
import random

def extended():
    class Ball:
        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r
            self.color = random.choice([arcade.color.YELLOW_ORANGE, arcade.color.APPLE_GREEN])
            self.xdir = random.random()*2
            self.ydir = random.random()*2

        def draw(self):
            arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

        def update(self, width, height):
            self.x += self.xdir
            self.y += self.ydir

            if (self.x + self.r) > width or (self.x - self.r) < 0:
                self.xdir *= -1
            if (self.y + self.r) > height or (self.y - self.r) < 0:
                self.ydir *= -1

        def change_col(self):
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))



    class MyPicture(arcade.Window):
        def __init__(self, width, height, title):
            arcade.Window.__init__(self, width, height, title)
            arcade.set_background_color(arcade.color.BLUE)
            
            self.width = width
            self.height = height

            self.balls = [Ball(self.width/2, self.height/2, 10) for i in range(50)]

            self.space_pressed = False

            arcade.run()

        def on_draw(self):
            arcade.start_render()
            for ball in self.balls:
                ball.draw()

        def on_update(self, dt):
            for ball in self.balls:
                ball.update(self.width, self.height)
                if self.space_pressed:
                    ball.change_col()

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.SPACE:
                self.space_pressed = True
            elif symbol == arcade.key.Q:
                    arcade.close_window()

        def on_key_release(self, key, mod):
            if key == arcade.key.SPACE:
                self.space_pressed = False


    MyPicture(500,500,'Hi!')

def platformer():
    class Game(arcade.Window):
        def __init__(self):
            arcade.Window.__init__(self, 500, 500, 'Game')
            arcade.set_background_color(arcade.color.DARK_LAVA)

            self.player_sprite = None
            self.terrain_list = None
            self.player_list = None

            self.setup()

        def setup(self):
            self.player_list = arcade.SpriteList()
            self.terrain_list = arcade.SpriteList()

            self.player_sprite = arcade.Sprite('Sprites/platformChar_idle.png', 1)
            self.player_sprite.center_x = 250
            self.player_sprite.center_y = 250
            self.player_list.append(self.player_sprite)

            for loc in [(100,100), (400,200), (200, 400)]:
                terrain = arcade.Sprite('Sprites/platformPack_tile019.png', 1)
                terrain.center_x, terrain.center_y = loc
                self.terrain_list.append(terrain)


            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.terrain_list, 0.5)


        def on_draw(self):
            arcade.start_render()
            self.player_list.draw()
            self.terrain_list.draw()

        def on_update(self, dt):
            self.player_list.update()
            self.physics_engine.update()

            if self.player_sprite.center_y < -50:
                self.player_sprite.center_y = 600

            if self.player_sprite.center_x < -25:
                self.player_sprite.center_x = 525
            if self.player_sprite.center_x > 525:
                self.player_sprite.center_x = -25

        def on_key_press(self, key, mod):
            if key == arcade.key.RIGHT:
                self.player_sprite.change_x = 2
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -2
            elif key == arcade.key.SPACE:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = 10
            elif key == arcade.key.Q:
                arcade.close_window()

        def on_key_release(self, key, mod):
            if key == arcade.key.RIGHT or key == arcade.key.LEFT:
                self.player_sprite.change_x = 0

    Game()
    arcade.run()

if __name__ == '__main__':
    # extended()
    platformer()
