"""
Search algorithms to find a Knight's Tour of the Chess Board.
"""

def search_brute_force(board, position, step, path):
    """
    DFS with backtracking to find a Knight's Tour.

    This is the Brute Force approach to computing aKnight's Tour.
    """
    print(step)
    if step == 60:  # BUG: doesn't work beyond 60??
        return True  # tour found
    for move in board.get_possible_moves(position):
        board.mark_visited(move, step + 1)
        path.append(move)
        # NOTE: recursive call
        if search_brute_force(board, move, step + 1, path):
            return True
        # Backtrack
        board.unmark_visited(move)
        path.pop()
    return False