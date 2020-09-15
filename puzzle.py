import sys
from solver import Solver

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.start = []
        self.goal = []
        self.algorithm = None

    def handler(self):
        self.input()
        self.algorithm_select()
        self.launcher()

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

    def algorithm_select(self):
        print("Select a Solving Algorithm (Input Number)\n1. Breadth First Search\n2. Gready Best First\n3. A* Misplaced Tiles\n4. A* Manhatten Distance")
        self.algorithm = int(input())

    def launcher(self):
        s = Solver(self.start, self.goal, self)
        if (self.algorithm != None):
            if (self.algorithm == 1):
                s.breadth()
            if (self.algorithm == 2):
                s.gready()
            if (self.algorithm == 3):
                s.atile()
            if (self.algorithm == 4):
                s.amanhattan()
        else: 
            quit()