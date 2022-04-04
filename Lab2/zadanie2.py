f = open("zadanie2.csv")
txt = f.readlines()

my_file = open('readme.txt', 'w')

new_list = []

index_list = []

# tworzenie tablicy bez pustych linii
for line in txt:
    if len(line[(line.find(',') + 1):]) == 1:
        pass
    else:
        new_list.append(line)

# tworzenie tablicy samych indeksów
for a in range(1, len(new_list)):
    x = new_list[a].split(',')
    index_list.append(int(x[0]))

# sortowanie
m = len(index_list)
for u in range(m):
    for v in range(m - u - 1):
        if index_list[v] > index_list[v + 1]:
            index_list[v], index_list[v + 1] = index_list[v + 1], index_list[v]
            new_list[v + 1], new_list[v + 2] = new_list[v + 2], new_list[v + 1]



# naprawianie indeksów
for a in range(len(index_list)):
    for b in range(a + 1, len(index_list)):
        if index_list[a] == index_list[b]:
            index_list[b] += 1





for line in new_list:
    my_file.write(line)

my_file.close()
