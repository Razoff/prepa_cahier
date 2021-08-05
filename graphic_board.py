import hashlib
from enum import Enum

"""
Enum class holding the name of all pieces
"""
class PieceName(Enum):
    PAWN = "p"
    ROOK = "R"
    KNIGHT = "K"
    BISHOP = "B"
    QUEEN = "Q"
    KING = "K"


"""
Class Piece
Each piece has a name a color and a pos
p_name: Piece name
white: boolean True if white 
row: row position
column: column position
"""
class Piece:
    def __init__(self, p_name, white, row, column):
        self.p_name = p_name
        self.white = white
        self.row = row
        self.column = column

    """
    print piece with all its component
    """
    def print_piece(self):
        if self.white:
            color = "White"
        else :
            color = "Black"
        print(self.p_name, color, self.row, self.column)

    """
    return piece coordinate
    if numerical is true return position as (int,int)
    if numerical is false return position as (str, int) 
    """
    def get_coord(self, numerical=False):
        if numerical:
            return int(self.row) - 1, ord(self.column) - 97
        else:
            return self.row, self.column

    """
    Short piece name is the form "letterColor" : Cw
    """
    def get_short_name(self):
        if self.white:
            color = "w"
        else :
            color = "b"

        return self.p_name.value + color

    """
    Get starting board position 
    """
    @staticmethod
    def get_starting_board():
        ret = []
        for row in ["2","7"]:
            for col in ["a", "b", "c", "d", "e", "f", "g", "h"] :
                if row == "2":
                    ret.append(Piece(PieceName.PAWN, True, row, col))
                else:
                    ret.append(Piece(PieceName.PAWN, False, row, col))

        for row in ["1", "8"] :
            ret.append(Piece(PieceName.ROOK, row == "1", row, "a"))
            ret.append(Piece(PieceName.KNIGHT, row == "1", row, "b"))
            ret.append(Piece(PieceName.BISHOP, row == "1", row, "c"))
            ret.append(Piece(PieceName.QUEEN, row == "1", row, "d"))
            ret.append(Piece(PieceName.KING, row == "1", row, "e"))
            ret.append(Piece(PieceName.BISHOP, row == "1", row, "f"))
            ret.append(Piece(PieceName.KNIGHT, row == "1", row, "g"))
            ret.append(Piece(PieceName.ROOK, row == "1", row, "h"))

        return ret


"""
Graphic board to print
TBU probably will be changed to FEN file type + external library to display board
"""
class GraphicBoard:
    def __init__(self, state=[]):
        if not state:
            self.board_state = Piece.get_starting_board()
        else:
            self.board_state = state.copy()

        self.graph_repr = self.get_graph_repr()
        self.board_hash = self.compute_board_hash()

    def get_graph_repr(self):
        board = [["--" for y in range(8)] for x in range(8)]

        for piece in self.board_state:
            row, col = piece.get_coord(True)
            board[row][col] = piece.get_short_name()

        return board

    def compute_board_hash(self):
        return hashlib.md5(str(self.graph_repr).encode())

    def print_board(self):

        for line in reversed(self.graph_repr):
            print(line, "\n")

        print("Hash", self.board_hash.hexdigest())


