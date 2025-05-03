"""
Visualizer object for a Knight's Tour.
"""

# frameworks
import tkinter as tk
from tkinter import PhotoImage

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
        
        # BUG: neither of these render anything
        # Try to load knight image (fall back to red dot if not found)
        try:
            self.knight_img = PhotoImage(file="assets/knight.png").subsample(8, 8)
            self.knight = self.canvas.create_image(0, 0, image=self.knight_img, anchor='nw')
        except:
            self.knight_img = None
            self.knight = self.canvas.create_oval(0, 0, 10, 10, fill='red')
        
        self.draw_board()
        # Create step texts with appropriate colors
        self.step_texts = []
        for i in range(8):
            row_texts = []
            for j in range(8):
                # Determine text color based on tile color
                color = 'black' if (i + j) % 2 == 0 else 'white'
                text_id = self.canvas.create_text(
                    j * 50 + 25, 
                    i * 50 + 25, 
                    text='',
                    fill=color,
                    font=('Arial', 10, 'bold')
                )
                row_texts.append(text_id)
            self.step_texts.append(row_texts)

    def draw_board(self):
        """Draw an 8x8 chessboard with alternating colors."""
        for i in range(8):
            for j in range(8):
                # Use traditional chessboard colors
                color = '#F0D9B5' if (i + j) % 2 == 0 else '#B58863'  # light and dark wood colors
                self.canvas.create_rectangle(
                    j * self.square_size, 
                    i * self.square_size,
                    (j + 1) * self.square_size, 
                    (i + 1) * self.square_size,
                    fill=color,
                    outline='black')

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
            
            if self.knight_img:
                # Move image to center of square
                self.canvas.coords(self.knight, x, y)
            else:
                # Move red dot
                self.canvas.coords(self.knight, x - 5, y - 5, x + 5, y + 5)
            
            self.canvas.itemconfig(self.step_texts[row][col], text=str(self.current_step + 1))
            self.current_step += 1
            self.window.after(500, self.move_knight)  # 500ms delay between moves