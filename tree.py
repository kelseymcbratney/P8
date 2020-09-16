class Tree:
    def __init__(self, name='root',children=None):
        self.name = name
        self.children = []
        if children is not None:
            for c in children:
                self.add_child(c)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
