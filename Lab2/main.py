tab = ''

for i in range (500, 700):
    if i % 7 == 0 and i % 5 != 0:
        tab+=str(i)

print(tab.count("21"))
print(tab.replace("21", "XX"))

