

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.open = []
        self.closed = []
        self.start = []
        self.goal = []

    def input(self):
        print("Input 3x3 Puzzle by Line - seperated by Spaces, and '_' as Blank. EG '5 7 _'")
        print("Start Puzzle")
        for i in range(0, self.size):
            print("Enter start line", i + 1)
            temp = input().split(' ')
            self.start.append(temp)
        print("Goal Puzzle")
        for i in range(0, self.size):
            print("Enter goal line", i + 1)
            temp = input().split(' ')
            self.goal.append(temp)



class Node:
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval







p = Puzzle(3)
p.input()

print(p.start, "\n", p.goal)