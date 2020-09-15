from tile import Tile

class Board:
    def __init__(self, values=[]):
        self.blank = None
        self.parity_val = None
        self.parity = None
    
    def make_graph(self):
         for x in values: