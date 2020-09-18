from que import Queue, PriorityQueue
from node import Node
from board import Board


class Solver:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.expanded = []
        self.closed = []
        self.que = Queue()
        self.pque = PriorityQueue()

    def expand(self, node):
        dict = {
            "up" : None,
            "down" : None,
            "left": None,
            "right" : None,
        }

        direction = ["up", "down", "left", "right"]
        solution = None
        for dir in direction:
            new_board = Board(node.data.values)
            if getattr(new_board.blank, dir) == None:
                continue
            new_board.move(dir)
            dict.update({dir:Node(new_board)})
            if dict[dir] == None:
                continue
            elif self.check_presence(dict[dir]):
                continue
            elif self.check_solution(dict[dir]):
                solution = dict[dir]
                break
            else:
                self.que.put_node(dict[dir])
                print("NEW NODE")
        return solution

    def check_solution(self, node):
        if node.data.values == self.goal:
            return True
        else:
            return False

    def check_presence(self, node):
        for x in self.expanded:
            print(node.data.values,"  first check ", x.data.values) #
            if node.data.values == x.data.values:
                print("true")
                return True

        current_node = self.que.head
        while not current_node == None:
            print(node.data.values," second check ", current_node.data.values) #
            if current_node.data.values == node.data.values:
                print("true")
                return True
            current_node = current_node.next
        return False
    
    def backtrace(self, node):
        """
            Funtion for traversing back up the tree. Will return an array 
            of the path taken starting from the start state
        """
        trace = []
        while not node == None:
            trace.append(node)
            node = node.parent
        trace.reverse()
        return trace

    def breadth(self):
        print("Breadth First")
        self.currentLevel = 1
        self.que.put_data(self.start)
        solution = None
        print("beginning")
        while self.que.head != None and solution == None:
            current_node = self.que.get()
            solution = self.expand(current_node)
            self.expanded.append(current_node)
        # Print Solution
        trace = self.backtrace(solution)
        for x in trace:
            x.data.print_board()


    def gready(self):
        pass

    def atile(self):
        
        self.pque.insert(Node(self.start))
        while not self.pque.isEmpty():
            current_node = self.pque.remove()
            self.calc_h(current_node.values,self.goal)
        
    

    def amanhattan(self):
        pass

    def calc_h(self, start, goal):
        temp = 0
        for i in range(0,len(start)):
            if (start[i] != goal[i] and start[i] != '_'):
                temp += 1
        return temp



