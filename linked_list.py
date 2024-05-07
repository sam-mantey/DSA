class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data = %s>" % self.data

class Linked_list:

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self, data, index):

        if index == 0: 
            self.add(data)
        
        if index > 0:

            new_node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            nextnode = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = nextnode
                

    def remove(self, key):
        found = False
        current = self.head
        previous = None

        while current and  not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current
    
    def remove_at_index(self, index):
        previous = None
        current = self.head

        if index == 0:
            self.head = current.next_node
            return current

        while index > 0:
            previous = current
            index -= 1
            current = current.next_node

        previous.next_node = current.next_node
        return current
        

        


           


                


            

        

    def __repr__(self):
        '''
        displays the content of the linked list
        '''
        current = self.head
        nodes = []

        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)

            current = current.next_node
        
        return " -> ".join(nodes)

