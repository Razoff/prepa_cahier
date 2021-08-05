class HalfMove:

    """
    Each member of this class hold half a move
    move_id: number of the full move the half move is part of (13)
    move_name: Name of the half move (Cxb2)
    white_move: True if it is a white move
    parent: parent half move
    children: list of all children half moves
    comment: Comment object if there is a comment None else
    graph_pos: TBU
    """
    def __init__(self, move_id, move_name, white_move, parent=None, children=[], comment=None, graph_pos=None):
        self.move_id = move_id
        self.move_name = move_name
        self.white_move = white_move
        self.parent = parent
        self.children = children
        self.comment = comment
        self.graph_pos = graph_pos

        # Full name is move_id. move_name for white and move_id... move name for black
        if white_move:
            self.full_name = str(self.move_id) + ". " + self.move_name
        else:
            self.full_name = str(self.move_id) + "... " + self.move_name

    """
    Print half move with or without comment
    """
    def print_half_move(self, comment=False):
        if comment:
            print(self.full_name, self.comment.comment)
        else :
            print(self.full_name)

    """
    Longer and more verbose print
    """
    def print_full_object(self):
        print("MOVE NAME", self.full_name)
        if self.comment is not None:
            print("COMMENT")
            self.comment.print_full_comment()
        if self.parent is not None:
            print("PARENT")
            self.parent.print_half_move()
        print("CHILDREN")
        for child in self.children:
            child.print_half_move()

