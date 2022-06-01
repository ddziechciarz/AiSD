from colorama import init, Fore, Back, Style

# # 0 1 2 3 4 5 coodrinate X
# 0
# 1
# 2
# 3
# 4
# 5
# coordinate Y

def read_data():
    #read data and automatically convert each field to int
    f = open("packages/packages100.txt")
    l = f.readlines()
    l = l[2:]

    products = []

    for line in l:
        new_line = []
        line = line.split(",")
        for element in line:
            new_line.append(int(element))
        products.append(new_line)
    return products

# def create_table(size):
#     table = []
#     for a in range(size):
#         new_line = []
#         for b in range(size):
#             new_line.append("#")
#         table.append(new_line)
#     return table
#
# def print_table(table:list):
#     for line in table:
#         print(line)


class Table:
    def __init__(self, size):
        #create 2D array of given size
        self.table = []
        for a in range(size):
            new_line = []
            for b in range(size):
                new_line.append("#")
            self.table.append(new_line)
        #self.i = 49

    def print_table(self):
        for line in self.table:
            for item in line:
                if item != "#":
                    letter_c = 30 + int(item) % 9
                    #bg = 49 - int(item) % 8
                    print(f'\033[{letter_c}m' + "X", "", end="")
                    #print(item, "", end="")
                else:
                    print("# ", end="")
            print("")

    def insert_item(self, product: list):
        for y in range(len(self.table)):
            for x in range(len(self.table[0])):
                if self.fit_item(x, y, product[0], product[1], product[2]):
                    return True
        return False

    def fit_item(self, x, y, id, width, height):
        if (y + height <= len(self.table)) and (x + width <= len(self.table[0])):
            for a in range(height):
                for b in range(width):
                    if self.table[y + a][x + b] != "#":
                        return False
            for a in range(height):
                for b in range(width):
                    self.table[y + a][x + b] = id
            return True

    def fill_table_naive(self, data: list):
        value = 0
        items_fitted = []
        data.sort(reverse=True, key=lambda item: item[3]/ item[1] * item[2])
        #sort data by descending value
        for item in data:
            if self.insert_item(item) is False:
                pass
            else:
                value += item[3]
                items_fitted.append(item[0])
        print(value)
        return items_fitted



if __name__ == '__main__':
    init(autoreset=True)
    products = read_data()

    new_table = Table(100)

    print(new_table.fill_table_naive(products))
    new_table.print_table()
    text = f"\0{30 + 3}[31m"
    print(f'\033[{33}m' + "HI")
