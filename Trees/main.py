import random
import math
import time

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data == self.data:
                return;
            elif data < self.data:
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

    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left is not None:
                return self.left.search(value)
            return False
        else:
            if self.right is not None:
                return self.right.search(value)
            return False

    def minimum(self):
        if self.left is None:
            return self.data
        else:
            return min(self.data, self.left.minimum())

    def maximum(self):
        if self.right is None:
            return self.data
        else:
            return max(self.data, self.right.maximum())


class Forest:
    def __init__(self, size):
        self.size = size
        self.roots = [None for i in range(size)]

    def insert_data(self, data):
        if self.roots[math.floor(data)] is None:
            self.roots[math.floor(data)] = Node(math.floor(data) + 0.5)
        self.roots[math.floor(data)].insert(data)

    def print_data(self):
        for tree in self.roots:
            if tree is not None:
                tree.print_tree()
                print("")

    def search(self, value):
        if value > self.roots[-1].data + 0.5 or value < self.roots[0].data:
            return False
        if self.roots[math.floor(value)] is None:
            return False
        for root in self.roots:
            if root is not None and root.search(value):
                return True
        #return self.roots[math.floor(value)].search(value)

    def min(self):
        i = 0
        while self.roots[i] is None:
            i += 1
        return self.roots[i].minimum()

    def max(self):
        i = self.size - 1
        while self.roots[i] is None:
            i -= 1
        return self.roots[i].maximum()

def test_case(test_size):
    times = {"insert time":0,
             "max time":0,
             "finding value time":0}

    Tree_size = 10
    test_values = [random.uniform(0, Tree_size) for i in range(test_size)]
    new_forest = Forest(Tree_size)
    insert_time = time.time()

    for value in test_values:
        new_forest.insert_data(value)

    times["insert time"] = time.time() - insert_time

    max_time = time.time()
    new_forest.max()

    times["max time"] = time.time() - max_time

    finding_time = time.time()
    new_forest.search(test_values[5])

    times["finding value time"] = time.time() - finding_time

    return times

if __name__ == "__main__":

    # FOREST_SIZE = 10
    #
    # forest = Forest(FOREST_SIZE)
    #
    # random_numbers = [round(random.uniform(0, FOREST_SIZE), 2) for i in range(50)]
    #
    # for number in random_numbers:
    #     forest.insert_data(number)
    #
    # forest.print_data()

    times = test_case(100000)
    print(times)







