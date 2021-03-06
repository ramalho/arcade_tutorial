import arcade

SPRITE_SCALING = 0.5


class Player(arcade.Sprite):
    def __init__(self, filename, scaling, screen_x, screen_y):
        super().__init__(filename, scaling)
        self.center_x = 0
        self.center_y = 0
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.velocity_x = 5
        self.velocity_y = 0

    def update(self):
        self.center_x += self.velocity_x
        self.center_y += self.velocity_y

        is_at_right = self.center_x > self.screen_x
        is_moving_right = self.velocity_x > 0
        if is_at_right and is_moving_right:
            self.velocity_x *= -1

        is_at_left = self.center_x < 1
        is_moving_left = self.velocity_x < 0
        if is_at_left and is_moving_left:
            self.velocity_x *= -1

        is_at_top = self.center_y > self.screen_y
        is_moving_up = self.velocity_y > 0
        if is_at_top and is_moving_up:
            self.velocity_y *= -1

        is_at_bottom = self.center_y < 1
        is_moving_down = self.velocity_y < 0
        if is_at_bottom and is_moving_down:
            self.velocity_y = 0

    def go_right(self):
        self.velocity_x = abs(self.velocity_x) * -1

    def go_left(self):
        self.velocity_x = abs(self.velocity_x)

    def go_up(self):
        self.velocity_y += 10


class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)

        # Make a player
        self.player = Player('examples/images/character.png', SPRITE_SCALING,
                             width, height)

        # Make a sprite list
        self.all_sprites_list = arcade.SpriteList()
        self.all_sprites_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def animate(self, delta_time):
        self.all_sprites_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.go_right()
        elif key == arcade.key.RIGHT:
            self.player.go_left()
        elif key == arcade.key.UP:
            self.player.go_up()


def main():
    game = MyGame(600, 600, 'Drawing Example', arcade.color.WHEAT)
    game.player.center_x = 1
    arcade.run()


if __name__ == '__main__':
    main()
