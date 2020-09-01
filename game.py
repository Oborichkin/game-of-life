import arcade

ROWS = 50
COLS = 50

WIDTH = HEIGHT = SIZE = 15
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

        self.frame_count = 0
        self.playing = False

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

    def on_update(self, dt):
        self.frame_count += 1
        if self.playing and self.frame_count % 10 == 0:
            self.evolve()

    def evolve(self):
        update_list = []

        for row in range(ROWS):
            for col in range(COLS):

                neighbours = 0
                for i in range(max(0, row-1), min(ROWS-1, row+2)):
                    for j in range(max(0, col-1), min(COLS-1, col+2)):
                        if i == row and j == col:
                            continue
                        if self.grid[i][j].color == arcade.color.GREEN:
                            neighbours += 1

                if self.grid[row][col].color == arcade.color.GREEN:
                    if neighbours not in (2, 3):
                        update_list.append((row, col, arcade.color.WHITE))
                else:
                    if neighbours == 3:
                        update_list.append((row, col, arcade.color.GREEN))

        for x, y, color in update_list:
            self.grid[x][y].color = color

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.playing = not self.playing

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