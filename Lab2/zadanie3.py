import time
wyraz = input("Podaj słowo:")

start_time = time.time()

f = open('SJP.txt')
txt = f.readlines()

while ' ' in wyraz:
    print("Podaj pojedyncze słowo:")
    wyraz = input("Podaj słowo:")

wyraz.lower()
wyraz += '\n'

for line in txt:
    if wyraz == line:
        print("Znaleziono słowo")
        break

print(time.time() - start_time)
