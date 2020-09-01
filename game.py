import arcade
import numpy as np

SCALE = 1

ROWS = 29 * 2
COLS = 21 * 2

SIZE = 20 / 2
MARGIN = 25
PADDING = 1 / 2

world = np.zeros((ROWS, COLS), dtype=int)

arcade.open_window(640, 480, "Game Of Life")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

for dx in range(ROWS):
    for dy in range(COLS):
        x = dx * (SIZE + PADDING) + MARGIN
        y = dy * (SIZE + PADDING) + MARGIN

        arcade.draw_rectangle_filled(x, y, SIZE, SIZE, color=arcade.color.GREEN)

arcade.finish_render()
arcade.run()

