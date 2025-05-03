"""
Search algorithms to find a Knight's Tour of the Chess Board.
"""

def search_brute_force(board, position, step, path, max_len=64):
    """
    DFS with backtracking to find a Knight's Tour.

    This is the Brute Force approach to computing aKnight's Tour.
    """
    if step == max_len:
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

def search_warnsdorff(board, position, step, path, max_len=64):
    """
    Find a Knight's Tour using Warnsdorff's Rule with backtracking.
    
    Args:
        board: Chessboard object with methods like get_possible_moves, mark_visited, unmark_visited
        position: Tuple (row, col) of current knight position
        step: Current step number in the tour
        path: List of positions in the tour
        max_len: Desired length of the tour (default 64 for 8x8 board)
    
    Returns:
        bool: True if a tour of max_len is found, False otherwise
    """
    if step == max_len:
        return True  # Tour of desired length found
    
    # Get possible moves and sort by Warnsdorff's heuristic (fewest onward moves)
    moves = board.get_possible_moves(position)
    moves.sort(key=lambda move: len(board.get_possible_moves(move)))
    
    for move in moves:
        board.mark_visited(move, step + 1)
        path.append(move)
        if search_warnsdorff(board, move, step + 1, path, max_len):
            return True
        # Backtrack
        board.unmark_visited(move)
        path.pop()
    return False

def solve_quadrant(board, start, size, start_row, start_col, step, path, quadrant_max_len):
    """
    Solve a Knight's Tour for a quadrant of size x size.
    
    Args:
        board: Chessboard object
        start: Starting position in the quadrant
        size: Size of the quadrant (e.g., 4 for 4x4)
        start_row: Starting row of the quadrant
        start_col: Starting column of the quadrant
        step: Current step in the quadrant tour
        path: List of positions in the quadrant tour
        quadrant_max_len: Desired length of the quadrant tour
    
    Returns:
        bool: True if quadrant tour is found, False otherwise
    """
    if step == quadrant_max_len:
        return True
    
    for move in board.get_possible_moves(start):
        if board.is_within_quadrant(move, size, start_row, start_col):
            board.mark_visited(move, step + 1)
            path.append(move)
            if solve_quadrant(board, move, size, start_row, start_col, step + 1, path, quadrant_max_len):
                return True
            # Backtrack
            board.unmark_visited(move)
            path.pop()
    return False

def find_connecting_move(board, from_pos, to_quad_start, quad_size, quad_start_row, quad_start_col):
    """
    Find a move from from_pos to a position within the target quadrant.
    
    Args:
        board: Chessboard object
        from_pos: Current position
        to_quad_start: Starting position of the target quadrant
        quad_size: Size of the quadrant
        quad_start_row: Starting row of the quadrant
        quad_start_col: Starting column of the quadrant
    
    Returns:
        tuple or None: Position in the target quadrant reachable from from_pos, or None if none exists
    """
    for move in board.get_possible_moves(from_pos):
        if board.is_within_quadrant(move, quad_size, quad_start_row, quad_start_col):
            return move
    return None

def search_divide_conquer(board, position, step, path, max_len=64):
    """
    Find a Knight's Tour using Divide-and-Conquer by solving quadrants and connecting them.
    
    Args:
        board: Chessboard object with methods like get_possible_moves, mark_visited, unmark_visited
        position: Tuple (row, col) of initial knight position
        step: Current step number in the tour
        path: List of positions in the tour
        max_len: Desired length of the tour (default 64 for 8x8 board)
    
    Returns:
        bool: True if a tour of max_len is found, False otherwise
    """
    quadrant_size = 4
    quadrant_max_len = quadrant_size * quadrant_size  # 16 for 4x4
    
    # Define quadrants: (start_row, start_col)
    quadrants = [(0, 0), (0, 4), (4, 0), (4, 4)]
    
    # Track visited quadrants
    current_pos = position
    current_step = step
    path.append(current_pos)
    board.mark_visited(current_pos, current_step)
    
    for quad_start_row, quad_start_col in quadrants:
        # Find a move to this quadrant from current position
        next_pos = find_connecting_move(board, current_pos, (quad_start_row, quad_start_col), 
                                       quadrant_size, quad_start_row, quad_start_col)
        if next_pos and current_step < max_len:
            current_step += 1
            board.mark_visited(next_pos, current_step)
            path.append(next_pos)
            current_pos = next_pos
            
            # Solve the quadrant
            quad_path = []
            if solve_quadrant(board, current_pos, quadrant_size, quad_start_row, quad_start_col, 
                             0, quad_path, quadrant_max_len):
                for i, pos in enumerate(quad_path, start=current_step + 1):
                    if current_step + i <= max_len:
                        board.mark_visited(pos, current_step + i)
                        path.append(pos)
                current_step += len(quad_path)
                current_pos = quad_path[-1] if quad_path else current_pos
                
                if current_step >= max_len:
                    return True
            else:
                # Backtrack if quadrant tour fails
                for pos in quad_path:
                    board.unmark_visited(pos)
                board.unmark_visited(next_pos)
                path.pop()
                current_step -= 1
                current_pos = path[-1] if path else position
    
    return current_step >= max_len