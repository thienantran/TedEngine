# Correcting the mistake in ChessBoard's initialize_board method
from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King


class ChessBoard:
    """Class to represent the chess board"""
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

    def initialize_board(self):
        """Initialize the chess board with pieces"""
        # Place pawns
        for i in range(8):
            self.board[1][i] = Pawn("Black")
            self.board[6][i] = Pawn("White")

        # Place rooks
        self.board[0][0] = self.board[0][7] = Rook("Black")
        self.board[7][0] = self.board[7][7] = Rook("White")

        # Place knights
        self.board[0][1] = self.board[0][6] = Knight("Black")
        self.board[7][1] = self.board[7][6] = Knight("White")

        # Place bishops
        self.board[0][2] = self.board[0][5] = Bishop("Black")
        self.board[7][2] = self.board[7][5] = Bishop("White")

        # Place queens
        self.board[0][3] = Queen("Black")
        self.board[7][3] = Queen("White")

        # Place kings
        self.board[0][4] = King("Black")
        self.board[7][4] = King("White")

    def print_board(self):
        """Print the chess board"""
        for row in self.board:
            print(" ".join(str(piece) if piece else "  " for piece in row))

# Initialize and print the chess board
chess_board = ChessBoard()
chess_board.print_board()
