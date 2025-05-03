class ChessBoard:
    def __init__(self, knight):
        """
        Initialize an 8x8 board with a Knight instance.
        """
        self.knight = knight
        self.board = [[0 for _ in range(8)] for _ in range(8)]  # 0 is unvisited, anything else is visited

    def is_within_bounds(self, position):
        """
        Check if a position is within the 8x8 board.
        """
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def is_visited(self, position):
        """
        Check if a position has been visited.
        """
        row, col = position
        return self.board[row][col] > 0

    def mark_visited(self, position, step):
        """
        Mark a position as visited with a step number.
        """
        row, col = position
        self.board[row][col] = step

    def unmark_visited(self, position):
        """
        Unmark a position (set step to 0).
        """
        row, col = position
        self.board[row][col] = 0

    def get_possible_moves(self, position):
        """
        Get all valid moves from a position.
        """
        offsets = self.knight.get_move_offsets()
        possible_moves = []
        for offset in offsets:
            new_row = position[0] + offset[0]
            new_col = position[1] + offset[1]
            new_position = (new_row, new_col)
            if self.is_within_bounds(new_position) and not self.is_visited(new_position):
                possible_moves.append(new_position)
        return possible_moves