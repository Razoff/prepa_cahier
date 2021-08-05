#!/usr/bin/env python3

import game
import headers
import half_move
import pgn_move_processing

import graphic_board

easy_pgn = "pgn_test/easy.pgn"
hard_pgn = "pgn_test/hard.pgn"
scandi_pgn = "pgn_test/scandi_facile.pgn"

print("\n-------- EASY PGN --------\n")

#header_easy = headers.Headers.get_headers_from_pgn(easy_pgn)
#header_easy.print_headers()
#easy_pgn_move = pgn_move_processing.PGNManipulator(easy_pgn)
#easy_pgn_move.process_file()
easy_game = game.Game.game_from_pgn(easy_pgn)
easy_game.print_all()
easy_game.make_graph()
easy_game.display_graph()

print("\n-------- HARD PGN --------\n")

#header_hard = headers.Headers.get_headers_from_pgn(hard_pgn)
#header_hard.print_headers()
#hard_pgn_move = pgn_move_processing.PGNManipulator(hard_pgn)
#hard_pgn_move.process_file()
hard_game = game.Game.game_from_pgn(hard_pgn)
hard_game.print_all()
hard_game.make_graph()
hard_game.display_graph()

print("\n-------- SCANDI PGN --------\n")

#header_scandi = headers.Headers.get_headers_from_pgn(scandi_pgn)
#header_scandi.print_headers()
#scandi_pgn_move = pgn_move_processing.PGNManipulator(scandi_pgn)
#scandi_pgn_move.process_file()
scandi_game = game.Game.game_from_pgn(scandi_pgn)
scandi_game.print_all()
scandi_game.make_graph()
scandi_game.display_graph()

print("\n-------- Others --------\n")

graphic_board.GraphicBoard().print_board()

