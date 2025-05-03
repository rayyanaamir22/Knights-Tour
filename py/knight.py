class Knight:
    def get_move_offsets(self):
        """Returns a list of possible move offsets for a knight."""
        return [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]