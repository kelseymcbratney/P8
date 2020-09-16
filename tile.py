class Tile:
    def __init__(self, val, position, up=None, down=None, left=None, right=None):
        self.val = val
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.position = position