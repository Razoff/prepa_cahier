import re
import half_move as hm
import comment as cmt

class PGNManipulator():

    """
    Init object and open .pgn file at path
    path: string to pgn file
    """
    def __init__(self, path):
        self.path = path
        self.pgn_file = open(self.path, "r")
        self.current_line = self.pgn_file.readline()
        self.current_text = self.setup_file()
        self.move_list = []

    """
    Move current_line to the next one
    """
    def next_line(self):
        self.current_line = self.pgn_file.readline()

    """
    Not clear yet
    """
    def process_file(self):
        self.process_moves(0)

    """
    Process a full move (one white one black) starting from start offset in current_text
    start: offset to last found move
    parents: add parents move
    """
    def process_moves(self, start=0, parent=None, white_move=True):
        # Find next string of form : NB.
        move_to = re.search(r'[0-9]{1,}\.', self.current_text[start:])
        black_processed = False

        # re.search returns None is there are no match
        if move_to is not None:
            # Get start of move offset
            current_id = start + move_to.start()

            # Start by grabing id and move name
            current_id, move_id, move_name = self.get_move_id_and_name(current_id)

            # Check if the currently processed move is not at the end of a variant
            if self.check_end_of_variant(current_id):
                nag = []
                comment = ""
            else:
                # If not check if there is a comment and/or nag
                current_id, nag, comment = self.get_nag_and_comment(current_id)

            # Once id name nags and comment is retrieved create move
            move = hm.HalfMove(move_id, move_name, white_move, parent, [], cmt.Comment(nag, comment), None)

            # to avoid segfaults children list of parent is updated by children themselves
            if parent is not None:
                parent.children.append(move)

            # Append generated move to global move list
            self.move_list.append(move)
            # Keep the color of last proceeded move to know the color of the next one
            last_process_color = white_move

            # Check again if after the comment there is the end of a variant
            if self.check_end_of_variant(current_id):
                return move_to

            # Need to declare it here to be used after
            b_move = None

            # Recursively process next moves and variants
            while True:
                current_id = self.skip_char(current_id)

                # ( mark the sart of a new variant
                if self.current_text[current_id] == "(":

                    # Depending on last processed move to compute next move color and parent
                    if black_processed :
                        self.process_moves(current_id, move, last_process_color)
                    else:
                        self.process_moves(current_id, parent, last_process_color)

                    # The variant is processed recursively therefore jump to the next regular half move
                    current_id = self.skip_variant(current_id)

                # If next move is a digit use last processed color to compute color and parent
                elif self.current_text[current_id].isdigit():
                    # New move inverse from the last one
                    # We get here if we have white move, comment, black move
                    # Recursively process next moves
                    if black_processed:
                        self.process_moves(current_id, b_move, not last_process_color)
                    else:
                        self.process_moves(current_id, move, not last_process_color)

                    # If we are here we have finish to process the full move moving to the next one
                    break

                # Detect if we are at the end of the file
                elif self.current_text[current_id] == "*" or (self.current_text[current_id] == "1" and (self.current_text[current_id+1] == "/" or self.current_text[current_id+1] == "-")):
                    return move_to

                # Else the structure is white_move black move with no comment in between
                else:
                    # Parse regular black move
                    current_id, b_move_name = self.get_move_name(current_id)
                    if self.check_end_of_variant(current_id):
                        b_nag = []
                        b_comment = ""
                    else:
                        current_id, b_nag, b_comment = self.get_nag_and_comment(current_id)

                    b_move = hm.HalfMove(move_id, b_move_name, False, move, [], cmt.Comment(b_nag, b_comment))

                    move.children.append(b_move)
                    self.move_list.append(b_move)
                    last_process_color = False
                    black_processed = True

                    if self.check_end_of_variant(current_id):
                        return move_to

        return move_to

    """
    Put 'pointer' on text after headers
    header line start all with a [
    """
    def skip_headers(self):
        while self.current_line[0] == "[":
            self.next_line()

    """
    Start at current_text[start+1] and check if this char is in to_skip do it until next char is not
    start : current offset in current_text
    to_skip : list of char to skip (might be empty)
    space : if True add space char into to_skip
    :returns id to continue analysis 
    """
    def skip_char(self, start, to_skip=[], space=True):
        ret = start
        tmp_to_skip = to_skip

        if space:
            tmp_to_skip.append(" ")

        while self.current_text[ret] in tmp_to_skip:
            ret = ret + 1

        return ret

    """
    Move from start to the end of the variant
    """
    def skip_variant(self, start):
        tmp_index = start+1  # Start one char after (
        to_match = 1  # Number of ) to find before the end of the variant

        # Get out of the loop when all ) from ( have been found
        while to_match != 0:
            # Jump until next ( or )
            tmp_index, check_str = self.get_until(tmp_index, ["(", ")"], False)

            # If a new variant start one more ) will need to be found
            if self.current_text[tmp_index] == "(":
                to_match = to_match + 1
                tmp_index = tmp_index + 1

            # if the end of a variant if found decrease the number of end of variant to find
            elif self.current_text[tmp_index] == ")":
                to_match = to_match - 1
                tmp_index = tmp_index + 1

            # Emergency else statement should never be here
            else:
                print("POURQUOI")

        return tmp_index

    """
    Goes from start index to . and return the number
    """
    def get_move_id(self, start):
        return self.get_until(start, ["."], False)

    """
    Get move name by skipping until space or nag or end of variant
    """
    def get_move_name(self, start):
        return self.get_until(start, ["!", "?",  ")"])

    """
    Combine both get_move_id and get_move_name
    """
    def get_move_id_and_name(self, start):
        id_index, id_name = self.get_move_id(start)
        id_m_name, id_m_name_name = self.get_move_name(self.skip_char(id_index, ["."]))

        return id_m_name, id_name, id_m_name_name

    """
    Return true if at start index we are at )
    """
    def check_end_of_variant(self, start):
        return self.current_text[start] == ")"

    """
    Returns index after the comment and both element to construct Comment object
    """
    def get_nag_and_comment(self, start):
        tmp_index = start
        ret_nag = []
        ret_comment = ""

        tmp_index, point_nag = self.get_until(tmp_index)
        translated_point_nag = self.get_translate_point_nag(point_nag)

        if translated_point_nag != "$":
            ret_nag.append(translated_point_nag)

        # Gather additional nags
        while True:
            tmp_index = self.skip_char(tmp_index)
            if self.current_text[tmp_index] == "$":
                tmp_index, tmp_nag = self.get_until(tmp_index)
                ret_nag.append(tmp_nag)
            elif self.current_text[tmp_index] == "{":
                tmp_index, tmp_nag = self.get_until(tmp_index, "}", False)
                ret_comment = tmp_nag[1:]  # To remove {
            else:
                if ret_comment != "":
                    tmp_index = tmp_index + 1
                return tmp_index, ret_nag, ret_comment

    """
    Orthogonal usage as skip_char. Instead of skipping it returns the chars until a char in until is found
    start: Start offset in current_text
    until: gather chars until a char in this array is found
    space: adds space char in until
    :returns new offset to continue analysis, char gathered along the way
    """
    def get_until(self, start, until=[], space=True):
        ret_id = start
        ret_str = ""

        if space:
            until.append(" ")

        while self.current_text[ret_id] not in until:
            ret_str = ret_str + self.current_text[ret_id]
            ret_id = ret_id + 1

        return ret_id, ret_str

    """
    Takes raw pgn file and return a single string with no header line jump tab or return
    """
    def setup_file(self):
        self.skip_headers()
        current_text = self.pgn_file.read()
        return current_text.replace("\n", " ").replace("\t", " ").replace("\r", " ")

    """
    Close and open pgn file again
    """
    def restart(self):
        self.pgn_file.close()
        self.pgn_file = open(self.path, "r")
        self.current_line = self.pgn_file.readline()

    """
    Custom destructor to close file when object is not needed anymore
    """
    def __del__(self):
        self.pgn_file.close()

    """
    Translate nag that are specific point to $nb format
    """
    @staticmethod
    def get_translate_point_nag(point_nag):
        if point_nag == "!":
            nag_nb = "1"
        elif point_nag == "?":
            nag_nb = "2"
        elif point_nag == "!!":
            nag_nb = "3"
        elif point_nag == "??":
            nag_nb = "4"
        elif point_nag == "!?":
            nag_nb = "5"
        elif point_nag == "?!":
            nag_nb = "6"
        else:
            nag_nb = ""

        return "$" + nag_nb
