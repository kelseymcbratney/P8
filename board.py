from tile import Tile

class Board:
    """
        The board class takes in an array of values for the board of the 
        puzzle. With these values it will create a graph of Tiles. This 
        class will also hold the parity of the board
    """
    def __init__(self, values=[]):
        self.blank = None
        self.values = values
        self.parity_val = self.__calc_parity()
        self.parity = None
        if self.__is_even(self.parity_val):
           self.parity = "even"
        else:
           self.parity = "odd"
        self.make_graph()
        self.__calc_parity()
    
    def __calc_parity(self):
        inversions = 0
        for x in range(8):
            if self.values[x] == "_":
                continue
            for y in range(x+1, len(self.values)):
                if self.values[y] == "_":
                    continue
                if self.values[x] > self.values[y]:
                    inversions += 1
        return inversions
                    

    def make_graph(self):
        """
            This function will create a graph of the board based on the 
            values that were given at initializaton.
            Building happens from left to right top to bottom
        """
        tile1 = self.__create_tile(self.values[0])
        tile2 = self.__create_tile(self.values[1], None, None, tile1)
        tile1.right = tile2 
        tile3 = self.__create_tile(self.values[2], None, None, tile2)
        tile2.right = tile3
        tile4 = self.__create_tile(self.values[3], tile1)
        tile1.down = tile4
        tile5 = self.__create_tile(self.values[4], tile2, None, tile4)
        tile4.right = tile5
        tile2.down = tile5
        tile6 = self.__create_tile(self.values[5], tile3, None, tile5)
        tile3.down = tile6
        tile5.right = tile6
        tile7 = self.__create_tile(self.values[6], tile4)
        tile4.down = tile7
        tile8 = self.__create_tile(self.values[7], tile5, None, tile7)
        tile5.down = tile8
        tile7.right = tile8
        tile9 = self.__create_tile(self.values[8], tile6, None, tile8)
        tile6.down = tile9
        tile8.right = tile9


    def __create_tile(self, val, up=None, down=None, left=None, right=None):
        """
            Helper function to create tiles for the board.
            Looks at each value to see if it contains the blank,
            when found it will add a reference to it with the 
            instance varible blank
        """
        if val == "_":
            self.blank = Tile(val, up, down, left, right)
            return self.blank
        else:
            return Tile(val, up, down, left, right)

    def __is_even(self, val):
        """
            Simple helper function to determine if passed value is even or odd
        """

        if val%2 == 0:
            return True
        else:
            return False