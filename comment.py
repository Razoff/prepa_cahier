class Comment:

    """
    Comment object it has two parameters
    nags: holds a list of nags if there are some under the form $nb
    comment: string comment
    """
    def __init__(self, nags=[], comment=""):
        self.nags = nags
        self.comment = comment

    """
    Print list of all nags
    """
    def print_nags(self):
        to_print = ""
        for elem in self.nags:
            to_print = to_print + elem + " "

        print(to_print)

    """
    Print comment string
    """
    def print_comment(self):
        print(self.comment)

    """
    Print full object : nags and comment string
    """
    def print_full_comment(self):
        if self.nags == [] and self.comment == "":
            return
        else:
            print("NAGs", self.print_nags(), "COMMENT", self.print_comment())

    """
    Translation table from $nb to human readable 
    """
    @staticmethod
    def translate_NAG(nag):
        # Comment on directly preceding move 0-9
        if nag == "$0":
            ret_str = "No annotation"
        elif nag == "$1":
            ret_str = "Good move (!)"
        elif nag == "$2":
            ret_str = "Poor move (?)"
        elif nag == "$3":
            ret_str = "Brilliant move (!!)"
        elif nag == "$4":
            ret_str = "Blunder (??)"
        elif nag == "$5":
            ret_str = "Speculative move (!?)"
        elif nag == "$6":
            ret_str = "Dubious move (?!)"
        elif nag == "$7":
            ret_str = "Forced move (□)"
        elif nag == "$8":
            ret_str = "Singular move"
        elif nag == "$9":
            ret_str = "Worst move"
        # Comment on position
        elif nag == "$10":
            ret_str = ""
        elif nag == "$11":
            ret_str = ""
        elif nag == "$12":
            ret_str = ""
        elif nag == "$13":
            ret_str = ""
        elif nag == "$14":
            ret_str = ""
        elif nag == "$15":
            ret_str = ""
        elif nag == "$16":
            ret_str = ""
        elif nag == "$17":
            ret_str = ""
        elif nag == "$18":
            ret_str = ""
        elif nag == "$19":
            ret_str = ""
        elif nag == "$20":
            ret_str = ""
        elif nag == "$21":
            ret_str = ""
        elif nag == "$22":
            ret_str = ""
        elif nag == "$23":
            ret_str = ""
        elif nag == "$24":
            ret_str = ""
        elif nag == "$25":
            ret_str = ""
        elif nag == "$26":
            ret_str = ""
        elif nag == "$27":
            ret_str = ""
        elif nag == "$28":
            ret_str = ""
        elif nag == "$29":
            ret_str = ""
        elif nag == "$30":
            ret_str = ""
        elif nag == "$31":
            ret_str = ""
        elif nag == "$32":
            ret_str = ""
        elif nag == "$33":
            ret_str = ""
        elif nag == "$34":
            ret_str = ""
        elif nag == "$35":
            ret_str = ""
        elif nag == "$36":
            ret_str = ""
        elif nag == "$37":
            ret_str = ""
        elif nag == "$38":
            ret_str = ""
        elif nag == "$39":
            ret_str = ""
        elif nag == "$40":
            ret_str = ""
        elif nag == "$41":
            ret_str = ""
        elif nag == "$42":
            ret_str = ""
        elif nag == "$43":
            ret_str = ""
        elif nag == "$44":
            ret_str = ""
        elif nag == "$45":
            ret_str = ""
        elif nag == "$46":
            ret_str = ""
        elif nag == "$47":
            ret_str = ""
        elif nag == "$48":
            ret_str = ""
        elif nag == "$49":
            ret_str = ""
        elif nag == "$50":
            ret_str = ""
        elif nag == "$51":
            ret_str = ""
        elif nag == "$52":
            ret_str = ""
        elif nag == "$53":
            ret_str = ""
        elif nag == "$54":
            ret_str = ""
        elif nag == "$55":
            ret_str = ""
        elif nag == "$56":
            ret_str = ""
        elif nag == "$57":
            ret_str = ""
        elif nag == "$58":
            ret_str = ""
        elif nag == "$59":
            ret_str = ""
        elif nag == "$60":
            ret_str = ""
        elif nag == "$61":
            ret_str = ""
        elif nag == "$62":
            ret_str = ""
        elif nag == "$63":
            ret_str = ""
        elif nag == "$64":
            ret_str = ""
        elif nag == "$65":
            ret_str = ""
        elif nag == "$66":
            ret_str = ""
        elif nag == "$67":
            ret_str = ""
        elif nag == "$68":
            ret_str = ""
        elif nag == "$69":
            ret_str = ""
        elif nag == "$70":
            ret_str = ""
        elif nag == "$71":
            ret_str = ""
        elif nag == "$72":
            ret_str = ""
        elif nag == "$73":
            ret_str = ""
        elif nag == "$74":
            ret_str = ""
        elif nag == "$75":
            ret_str = ""
        elif nag == "$76":
            ret_str = ""
        elif nag == "$77":
            ret_str = ""
        elif nag == "$78":
            ret_str = ""
        elif nag == "$79":
            ret_str = ""
        elif nag == "$80":
            ret_str = ""
        elif nag == "$81":
            ret_str = ""
        elif nag == "$82":
            ret_str = ""
        elif nag == "$83":
            ret_str = ""
        elif nag == "$84":
            ret_str = ""
        elif nag == "$85":
            ret_str = ""
        elif nag == "$86":
            ret_str = ""
        elif nag == "$87":
            ret_str = ""
        elif nag == "$88":
            ret_str = ""
        elif nag == "$89":
            ret_str = ""
        elif nag == "$90":
            ret_str = ""
        elif nag == "$91":
            ret_str = ""
        elif nag == "$92":
            ret_str = ""
        elif nag == "$93":
            ret_str = ""
        elif nag == "$94":
            ret_str = ""
        elif nag == "$95":
            ret_str = ""
        elif nag == "$96":
            ret_str = ""
        elif nag == "$97":
            ret_str = ""
        elif nag == "$98":
            ret_str = ""
        elif nag == "$99":
            ret_str = ""
        elif nag == "$100":
            ret_str = ""
        elif nag == "$101":
            ret_str = ""
        elif nag == "$102":
            ret_str = ""
        elif nag == "$103":
            ret_str = ""
        elif nag == "$104":
            ret_str = ""
        elif nag == "$105":
            ret_str = ""
        elif nag == "$106":
            ret_str = ""
        elif nag == "$107":
            ret_str = ""
        elif nag == "$108":
            ret_str = ""
        elif nag == "$109":
            ret_str = ""
        elif nag == "$110":
            ret_str = ""
        elif nag == "$111":
            ret_str = ""
        elif nag == "$112":
            ret_str = ""
        elif nag == "$113":
            ret_str = ""
        elif nag == "$114":
            ret_str = ""
        elif nag == "$115":
            ret_str = ""
        elif nag == "$116":
            ret_str = ""
        elif nag == "$117":
            ret_str = ""
        elif nag == "$118":
            ret_str = ""
        elif nag == "$119":
            ret_str = ""
        elif nag == "$120":
            ret_str = ""
        elif nag == "$121":
            ret_str = ""
        elif nag == "$122":
            ret_str = ""
        elif nag == "$123":
            ret_str = ""
        elif nag == "$124":
            ret_str = ""
        elif nag == "$125":
            ret_str = ""
        elif nag == "$126":
            ret_str = ""
        elif nag == "$127":
            ret_str = ""
        elif nag == "$128":
            ret_str = ""
        elif nag == "$129":
            ret_str = ""
        elif nag == "$130":
            ret_str = ""
        elif nag == "$131":
            ret_str = ""
        elif nag == "$132":
            ret_str = ""
        elif nag == "$133":
            ret_str = ""
        elif nag == "$134":
            ret_str = ""
        elif nag == "$135":
            ret_str = ""
        # Comment on zeitnot
        elif nag == "$136":
            ret_str = ""
        elif nag == "$137":
            ret_str = ""
        elif nag == "$138":
            ret_str = ""
        elif nag == "$139":
            ret_str = "Black has severe time control pressure / zeitnot"
        else:
            ret_str = "None standard NAG"

        return ret_str
