"""
Launch a search agent and visualize the results.
"""

# utils
from board import ChessBoard
from knight import Knight
from search import search_brute_force, search_warnsdorff, search_divide_conquer
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
    # NOTE: for search_brute_force, max_len=64 (full knight's tour) takes really long. try <=60 for a quick partial tour.
    if search_divide_conquer(board, start_position, 1, path):  
        print(f"Tour found with {len(path)} steps.")
        visualizer = ChessBoardVisualizer()
        visualizer.animate_tour(path)
        visualizer.window.mainloop()
    else:
        # no Knight's Tour was found by this search
        print(f"No solution found: {path}")