class HalfMove:
    def __init__(self, move_id, move_name, white_move, parent=None, children=[], comment=None, graph_pos=None):
        self.move_id = move_id
        self.move_name = move_name
        self.white_move = white_move
        self.parent = parent
        self.children = children
        self.comment = comment
        self.graph_pos = graph_pos

        if white_move:
            self.full_name = str(self.move_id) + ". " + self.move_name
        else:
            self.full_name = str(self.move_id) + "... " + self.move_name

    def print_half_move(self, comment=False):
        if comment:
            print(self.full_name, self.comment.comment)
        else :
            print(self.full_name)

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

