class ChessPiece:
    """Base class for all chess pieces."""
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color[0]}{self.name[0]}"

    # Future methods for movement rules will be added here

class Pawn(ChessPiece):
    """Class representing a pawn."""
    def __init__(self, color):
        super().__init__(color, "Pawn")

class Rook(ChessPiece):
    """Class representing a rook."""
    def __init__(self, color):
        super().__init__(color, "Rook")

class Knight(ChessPiece):
    """Class representing a knight."""
    def __init__(self, color):
        super().__init__(color, "Knight")

class Bishop(ChessPiece):
    """Class representing a bishop."""
    def __init__(self, color):
        super().__init__(color, "Bishop")

class Queen(ChessPiece):
    """Class representing a queen."""
    def __init__(self, color):
        super().__init__(color, "Queen")

class King(ChessPiece):
    """Class representing a king."""
    def __init__(self, color):
        super().__init__(color, "King")

# Additional methods for movement and special rules can be added to each class
