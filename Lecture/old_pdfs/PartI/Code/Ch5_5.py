def u_check():
    A = [
            {'name': 'Jill', 'weight':125, 'height':62},
            {'name': 'Sam', 'weight':156, 'height':68},
            {'name': 'Bobby', 'weight':173, 'height':75},
        ]
    A.append({'weight':204, 'height':70, 'name':'Jim'})
    B = A[1]
    B['weight'] = 167
    # D = {'name': 'James', 'weight':245, 'height':77}
    # A[2].update(D)
    del A[0]['weight']
    C = [d.get('weight',100) for d in A]

    print(C)


def sets_examples():
    A = {1,2,3,4,5,6,7,7,7,7,7}
    B = {1,3,5,7,9}

    print(len(A))
    for v in B:
        print(v)

    print(A.union(B))

    print(A.intersection(B))

    C = [1,3,3,3,5]
    print(5 in set(C))
    print(set(C).issubset(B))


def arcade_sprites():
    import arcade

    def main():
        global sprites
        arcade.open_window(500, 300, 'Sprites and SpriteLists')
        arcade.set_background_color(arcade.color.GREEN_YELLOW)

        truck = arcade.Sprite('pngs/truckcabin.png', 1.5, center_x=250, center_y=150)
        truck.change_x = 1

        hotdogs = arcade.Sprite('pngs/hotdog.png', scale=1.5, center_x=200, center_y=50)
        hotdogs.change_x = 1
        hotdogs.change_y = 1

        iamabus = arcade.Sprite('pngs/bus_school.png', scale=1.5, center_x=100, center_y=200)
        iamabus.change_x, iamabus.change_y = -1, 2

        sprites = arcade.SpriteList()
        sprites.append(truck)
        sprites.append(hotdogs)
        sprites.append(iamabus)

        arcade.schedule(on_draw, 1/60)

        arcade.run()

    def on_draw(dt):
        arcade.start_render()

        sprites.draw()
        sprites.update()

        for sprite in sprites:
            if sprite.right > 500 or sprite.left < 0:
                sprite.change_x *= -1
            if sprite.top > 300 or sprite.bottom < 0:
                sprite.change_y *= -1

            if sprite.collides_with_list(sprites):
                sprite.turn_right()
                # sprite.kill()

        arcade.finish_render()

    def alt():
        global truck
        arcade.open_window(500, 300, 'Sprites and SpriteLists')
        arcade.set_background_color(arcade.color.GREEN)

        truck = arcade.Sprite('pngs/truckcabin.png', 5, center_x=250, center_y=150)
        arcade.start_render()
        truck.draw()
        arcade.finish_render()

        arcade.run()


    main()

if __name__ == '__main__':
    # u_check()
    # sets_examples()
    arcade_sprites()
