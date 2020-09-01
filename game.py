import arcade

ROWS = 25
COLS = 25

WIDTH = HEIGHT = SIZE = 25
MARGIN = 1

SCREEN_WIDTH = (WIDTH + MARGIN) * COLS + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROWS + MARGIN
SCREEN_TITLE = "Game Of Life"


class GameOfLife(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList()
        self.grid = []

        for row in range(ROWS):
            self.grid.append([])
            for col in range(COLS):
                x = (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
                sprite.center_x, sprite.center_y = x, y
                self.sprite_list.append(sprite)
                self.grid[row].append(sprite)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        column = int(x // (MARGIN + WIDTH))
        row = int(y // (MARGIN + HEIGHT))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if row < ROWS and column < COLS:

            if self.grid[row][column].color == arcade.color.WHITE:
                self.grid[row][column].color = arcade.color.GREEN
            else:
                self.grid[row][column].color = arcade.color.WHITE


def main():
    GameOfLife(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()