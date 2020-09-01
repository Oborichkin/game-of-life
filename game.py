import arcade
import numpy as np

ROWS = 25
COLS = 25

SIZE = 25
MARGIN = 1

WIDTH = (SIZE + MARGIN) * COLS + MARGIN
HEIGHT = (SIZE + MARGIN) * ROWS + MARGIN
TITLE = "Game Of Life"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.grid = np.zeros((ROWS, COLS), dtype=int)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        for row in range(ROWS):
            for column in range(COLS):

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.BLACK

                x = (MARGIN + SIZE) * column + MARGIN + SIZE // 2
                y = (MARGIN + SIZE) * row + MARGIN + SIZE // 2

                arcade.draw_rectangle_filled(x, y, SIZE, SIZE, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = int(x // (SIZE + MARGIN))
        row = int(y // (SIZE + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if row < ROWS and column < COLS:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    MyGame(WIDTH, HEIGHT, TITLE)
    arcade.run()


if __name__ == "__main__":
    main()