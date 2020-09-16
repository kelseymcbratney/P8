from node import Node
class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        
    def put(self, data, parent=None):
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
        self.head = old_head.next
        return old_head
    