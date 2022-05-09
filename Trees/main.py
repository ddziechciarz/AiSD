import random

NUM_SPACE = 5

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    #print(f"Inserted {data}")
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                    #print(f"Inserted {data}")
                else:
                    self.right.insert(data)

    def print_data(self, level=0):
        if self.left is None and self.right is None:
            print("-"*level, self.data)
            return
        else:
            if self.left is not None:
                self.left.print_data(level=level+1)
            if self.right is not None:
                self.right.print_data(level=level+1)
            print("-"*level, self.data)

    def print_tree(self, level=0):
        if level > 0:
            a = NUM_SPACE - (len(str(self.data)) + level)
            print(" " * a, ("-" * level), self.data, end="", sep="")
        else:
            print(self.data, end="", sep="")
        if self.left is not None:
            self.left.print_tree(level=level+1)
        if self.right is not None:
            print("")
            self.right.print_tree(level=level+1)


numbers = [random.randint(0, 20) for i in range(10)]

root = Node(numbers[0])

for i in range(1, len(numbers)):
    root.insert(numbers[i])

root.print_tree()






