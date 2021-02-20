class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node 

    def insert_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_link(self.head_node)
        self.head_node = new_node 

    def stringify_lst(self):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print(current_node.get_value().peek())                         ### Must print the top stack   ###
            current_node = current_node.get_link()
        
    def remove_node(self, value):
        current_node = self.get_head_node()
        if current_node.get_value() == value:
            self.head_node = current_node.get_link()
        else:
            while current_node:
                next_node = current_node.get_link()
                if next_node.get_value() == value:
                    current_node.set_link(next_node.get_link())
                    current_node = None 
                else:
                    current_node = next_node 

class Stack:
    def __init__(self, top_item=None):
        self.top_item = top_item 
        self.limit = 1000
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True 

    def has_space(self):
        if self.limit > self.size:
            return True 

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("The stack is empty")                     #### Anotation needs to be changed ####

    def push(self, new_value):
        if self.has_space() == True:
            new_node = Node(new_value)
            new_node.set_link(self.top_item)
            self.top_item = new_node 
            self.size =+ 1
        else:
            print('The stack is full')                      #### Anotation needs to be changed ####

    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_link()
            self.size -= 1
            return item_to_remove
        else:
            print("The stack is empty")                     #### Anotation needs to be changed ####
        


ll = LinkedList('a')

ll.insert_node('b')
ll.insert_node('c')
ll.remove_node('c')
#print(ll.stringify_lst())


s = Stack()

s.push('a')
s.push('b')
s.push('c')
s.pop()
#print(s.peek())



s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)

ll1 = LinkedList()

ll1.insert_node(s1)

s2 = Stack()
s2.push(4)
s2.push(5)
s2.push(6)

ll1.insert_node(s2)

print(ll1.stringify_lst())