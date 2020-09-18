from node import Node
class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        
    def put_data(self, data, parent=None):
        """ 
            This function will put some data into a Node 
            and insert that to the tail 
        """
        new_node = Node(data, parent)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.insert_behind(self.tail, new_node)
        
    def put_node(self, node, parent=None):
        if parent != None:
            node.parent = parent
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.insert_behind(self.tail, node)


    def insert_behind(self, current_node, new_node):
        """
            This function takes as input a Node that is inside the Queue
            as well as the Node to be inserted. It will then insert 
            the new Node directly behind the already existing Node.
        """
        if current_node.next == None:
            # If there is no next node then make the new node the tail
            current_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def get(self):
        """
            get() will return the head of the queue and remove it from the 
            queue.
        """
        old_head = self.head
        if self.head == self.tail:
            self.tail = None
        self.head = old_head.next
        return old_head

    def isEmpty(self):
        if (self.head == None):
            return True
        else:
            return False


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)

    def remove(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i].get_priority() < self.queue[max].get_priority():
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item
