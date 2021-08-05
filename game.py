import headers
import pgn_move_processing
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

class Game:
    def __init__(self, header, moves):
        self.header = header
        self.moves = moves
        self.pgn_graph = nx.Graph()
        self.label_dict = {}
        self.color_dict = {}

    def print_all(self):
        self.header.print_headers()
        print("\n")

        for move in self.moves:
            move.print_full_object()
            print("\n")

    def make_graph(self):
        self.add_move(self.find_first_move())

    def display_graph(self):
        print(nx.get_node_attributes(self.pgn_graph, self.find_first_move()))
        values = [self.color_dict.get(node, 0.25) for node in self.pgn_graph.nodes()]
        print(values)
        pos = graphviz_layout(self.pgn_graph, prog="dot")
        nx.draw(self.pgn_graph, pos, labels=self.label_dict, with_labels=True, node_color=values, cmap=plt.cm.Greys)
        plt.show()

    def find_first_move(self):
        for move in self.moves:
            if move.parent is None:
                move.print_full_object()
                return move

    def add_move(self, move):
        self.pgn_graph.add_node(move)
        self.label_dict[move] = move.move_name
        if move.white_move:
            self.color_dict[move] = 0.0
        else:
            self.color_dict[move] = 2.0

        if move.parent is not None:
            self.pgn_graph.add_edge(move.parent, move)

        for child in move.children:
            self.add_move(child)

    @staticmethod
    def game_from_pgn(path):
        head = headers.Headers.get_headers_from_pgn(path)
        moves = pgn_move_processing.PGNManipulator(path)
        moves.process_file()

        return Game(head, moves.move_list)
