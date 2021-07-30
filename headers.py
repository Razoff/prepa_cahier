class Headers:

    """
    event, site, round, white/black player and result are mandatory fields in PGNs files
    there are additional fields that can be passed through additional tags
    """
    def __init__(self, event, site, date, game_round, w_player, b_player, result,
                 additional_tags={}):
        self.event = event
        self.site = site
        self.date = date
        self.game_round = game_round
        self.w_player = w_player
        self.b_player = b_player
        self.result = result

        self.additional_tags = additional_tags

    """
    Get header dict for exact PGN mandatory fields + additional fields
    """
    def get_header_dict(self):
        ret = {"Event": self.event, "Site": self.site, "Date": self.date, "Round": self.game_round,
               "White": self.w_player, "Black": self.b_player, "Result": self.result}

        return ret | self.additional_tags

    """
    Pretty print of headers
    """
    def print_headers(self):
        for header, elem in self.get_header_dict().items():
            print(header, ":", elem)

    """
    This function is a static method to generate a Headers object from any pgn file
    pgn_path: String to .pgn file
    """
    @staticmethod
    def get_headers_from_pgn(pgn_path):
        # Mandatory headers to create headers
        mando_headers = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        tags = {}

        with open(pgn_path, "r") as pgn_file:
            line = pgn_file.readline()

            # Headers are the first line of the file and always statring with a [
            while line[0] == '[':
                # Header format: [Tag "elem"]\n
                tag = line.split(" ")[0][1:]
                elem = line.split("\"")[1]
                tags[tag] = elem
                line = pgn_file.readline()

        # Will contrain only non mandatory header for additonal_tags argument
        additional_args = tags.copy()

        # Remove mandatory arguments
        for mando in mando_headers:
            additional_args.pop(mando)

        return Headers(*[tags[tag] for tag in mando_headers], additional_tags=additional_args)
