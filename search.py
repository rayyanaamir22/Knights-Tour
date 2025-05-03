"""
Search algorithms to find a Knight's Tour of the Chess Board.
"""

def search_brute_force(board, position, step, path):
    """
    Brute force recursive backtracking to find a Knight's Tour.
    """
    if step == 64:
        return True  # Tour found
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