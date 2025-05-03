"""
Visualizer object for a Knight's Tour.
"""

# frameworks
import tkinter as tk

class ChessBoardVisualizer:
    def __init__(self):
        """
        Initialize the Tkinter window and canvas.
        """
        self.window = tk.Tk()
        self.window.title("Knight's Tour Simulation")
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        self.square_size = 50
        self.draw_board()
        self.knight = self.canvas.create_oval(0, 0, 10, 10, fill='red')
        self.step_texts = [[self.canvas.create_text(j * 50 + 25, i * 50 + 25, text='')
                           for j in range(8)] for i in range(8)]

    def draw_board(self):
        """Draw an 8x8 chessboard with alternating colors."""
        for i in range(8):
            for j in range(8):
                color = 'white' if (i + j) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(j * self.square_size, i * self.square_size,
                                            (j + 1) * self.square_size, (i + 1) * self.square_size,
                                            fill=color)

    def animate_tour(self, sequence):
        """Animate the knight's tour based on the sequence."""
        self.sequence = sequence
        self.current_step = 0
        self.move_knight()

    def move_knight(self):
        """Move the knight to the next position in the sequence."""
        if self.current_step < len(self.sequence):
            pos = self.sequence[self.current_step]
            row, col = pos
            x = col * self.square_size + self.square_size / 2
            y = row * self.square_size + self.square_size / 2
            self.canvas.coords(self.knight, x - 5, y - 5, x + 5, y + 5)
            self.canvas.itemconfig(self.step_texts[row][col], text=str(self.current_step + 1))
            self.current_step += 1
            self.window.after(500, self.move_knight)  # 500ms delay between moves