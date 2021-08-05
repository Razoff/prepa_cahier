import headers
import pgn_move_processing
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

"""
Game class. A game is a header object and and list of half_move objects
"""
class Game:
    def __init__(self, header, moves):
        self.header = header
        self.moves = moves
        self.pgn_graph = nx.Graph()
        self.label_dict = {}
        self.color_dict = {}

    """
    Print all object : headers and then moves
    """
    def print_all(self):
        self.header.print_headers()
        print("\n")

        for move in self.moves:
            move.print_full_object()
            print("\n")

    """
    Create graph of game by recursively process move and adding them to the graph
    """
    def make_graph(self):
        self.add_move(self.find_first_move())

    """
    Get pgn_graph element setup colors and label and show it
    """
    def display_graph(self):
        print(nx.get_node_attributes(self.pgn_graph, self.find_first_move()))
        values = [self.color_dict.get(node, 0.25) for node in self.pgn_graph.nodes()]
        print(values)
        pos = graphviz_layout(self.pgn_graph, prog="dot")
        nx.draw(self.pgn_graph, pos, labels=self.label_dict, with_labels=True, node_color=values, cmap=plt.cm.Greys)
        plt.show()

    """
    Find first move of the game in the list of moves by looking which move has no parent
    """
    def find_first_move(self):
        for move in self.moves:
            if move.parent is None:
                move.print_full_object()
                return move

    """
    Add move and recursively add its children to the graph with correct edges
    """
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

    """
    Return a Game object from a path to a pgn file
    """
    @staticmethod
    def game_from_pgn(path):
        head = headers.Headers.get_headers_from_pgn(path)
        moves = pgn_move_processing.PGNManipulator(path)
        moves.process_file()

        return Game(head, moves.move_list)
