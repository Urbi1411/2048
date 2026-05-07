import tkinter as tk
from logic import *

SIZE = 4
CELL = 100


class Game:
    def __init__(self, root):
        self.root = root

        self.canvas = tk.Canvas(
            root,
            width=SIZE * CELL,
            height=SIZE * CELL
        )
        self.canvas.pack()

        self.grid = [[0] * SIZE for _ in range(SIZE)]

        gen_new_tile(self.grid)
        gen_new_tile(self.grid)

        self.draw()

        root.bind("<Key>", self.on_key)

    def draw(self):
        self.canvas.delete("all")

        for i in range(SIZE):
            for j in range(SIZE):
                x0 = j * CELL
                y0 = i * CELL
                x1 = x0 + CELL
                y1 = y0 + CELL

                value = self.grid[i][j]

                self.canvas.create_rectangle(
                    x0,
                    y0,
                    x1,
                    y1,
                    fill="lightgray"
                )

                if value != 0:
                    self.canvas.create_text(
                        x0 + CELL // 2,
                        y0 + CELL // 2,
                        text=str(value),
                        font=("Arial", 20, "bold")
                    )

    def show_message(self, text):
        self.canvas.create_rectangle(
            50,
            150,
            350,
            250,
            fill="white",
            outline="black",
            width=3
        )

        self.canvas.create_text(
            SIZE * CELL // 2,
            SIZE * CELL // 2,
            text=text,
            font=("Arial", 28, "bold"),
            fill="red"
        )

    def on_key(self, event):
        key = event.keysym.lower()

        if key not in ['w', 'a', 's', 'd']:
            return

        old = [row[:] for row in self.grid]

        self.grid = move(self.grid, key)

        if self.grid != old:
            gen_new_tile(self.grid)

        self.draw()

        if has_2048(self.grid):
            self.show_message("YOU WON!")
            self.root.unbind("<Key>")

        elif is_grid_full(self.grid) and not can_merge(self.grid):
            self.show_message("GAME OVER")
            self.root.unbind("<Key>")


root = tk.Tk()
root.title("2048")

game = Game(root)

root.mainloop()