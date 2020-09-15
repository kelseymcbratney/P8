class Node:
    def __init__(self, data=None, parent=None, next=None, level=None,fval=None):
        self.data = data
        self.level = level
        self.fval = fval
        self.parent = parent
        self.next = next

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
