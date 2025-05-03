"""
Launch a search agent and visualize the results.
"""

# utils
from board import ChessBoard
from knight import Knight
from search import search_brute_force
from visualizer import ChessBoardVisualizer

# driver
if __name__ == '__main__':
    # configs
    start_position = (0,0)
    knight = Knight()
    board = ChessBoard(knight)
    board.mark_visited(start_position, 1)
    path = [start_position]

    # attempt search (change to whatever search you want)
    if search_brute_force(board, start_position, 1, path):
        print(f"Tour found with {len(path)} steps.")
        visualizer = ChessBoardVisualizer()
        visualizer.animate_tour(path)
        visualizer.window.mainloop()
    else:
        # no Knight's Tour was found by this search
        print(f"No solution found: {path}")