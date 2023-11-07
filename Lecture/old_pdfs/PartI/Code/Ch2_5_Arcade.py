# Arcade Examples

# Smiley face

import arcade

arcade.open_window(600,600, 'FACE')

arcade.set_background_color(arcade.color.BLIZZARD_BLUE)
arcade.start_render()

arcade.draw_circle_filled(300,300, 200, arcade.color.YELLOW)

#eyes
arcade.draw_circle_filled(350, 350, 35, arcade.color.WHITE)
arcade.draw_circle_filled(250, 350, 35, arcade.color.WHITE)

arcade.draw_circle_filled(350, 350, 15, arcade.color.BLACK)
arcade.draw_circle_filled(250, 350, 15, arcade.color.BLACK)

#mouth
arcade.draw_arc_outline(300, 200, 200,100, arcade.color.BLACK, 0, 180)




arcade.finish_render()

arcade.run()
