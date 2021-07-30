import headers
import pgn_move_processing

class Game:
    def __init__(self, header, moves):
        self.header = header
        self.moves = moves

    def print_all(self):
        self.header.print_headers()
        print("\n")

        for move in self.moves:
            move.print_full_object()
            print("\n")

    @staticmethod
    def game_from_pgn(path):
        head = headers.Headers.get_headers_from_pgn(path)
        moves = pgn_move_processing.PGNManipulator(path)
        moves.process_file()

        return Game(head, moves.move_list)
