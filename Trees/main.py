import random
import math

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data <= self.data:
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

    # def print_data(self, level=0):
    #     if self.left is None and self.right is None:
    #         print("-"*level, self.data)
    #         return
    #     else:
    #         if self.left is not None:
    #             self.left.print_data(level=level+1)
    #         if self.right is not None:
    #             self.right.print_data(level=level+1)
    #         print("-"*level, self.data)

    def print_tree(self, level=0, offset=0):
        chars = offset + len(str(self.data)) + level
        if level > 0:

            print(("-" * level), self.data, end="", sep="")
        else:
            print(self.data, end="")
        if self.left is not None:
            self.left.print_tree(level=level+1, offset=chars)
        if self.right is not None:
            print("")
            print(" "*chars, end="")
            self.right.print_tree(level=level+1,offset=chars)

class Forest:
    def __init__(self, size):
        self.roots = [Node(0.5 + i) for i in range(size)]

    def insert_data(self, data):
        for tree in self.roots:
            if math.floor(tree.data) == math.floor(data):
                tree.insert(data)

    def print_data(self):
        for tree in self.roots:
            tree.print_tree()
            print("")


if __name__ == "__main__":
    FOREST_SIZE = 10

    forest = Forest(FOREST_SIZE)

    random_numbers = [round(random.uniform(0, FOREST_SIZE), 2) for i in range(50)]

    for number in random_numbers:
        forest.insert_data(number)

    forest.print_data()


# numbers = [random.randint(0, 100) for i in range(20)]
#
# root = Node(numbers[0])
#
# for i in range(1, len(numbers)):
#     root.insert(numbers[i])
#
# root.print_tree()






