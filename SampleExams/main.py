import random

class Lotto:
    def __init__(self, amount):
        self.numbers = [random.randint(0,48) for i in range (amount)]

    def check(self, lotto):
        matching_array = lotto.numbers
        for number in self.numbers:
            if number in matching_array:
                matching_array.remove(number)
            else:
                return False
        return True

    @classmethod
    def calc_prob(self, sample_size):
        succ_tries = 0
        for i in range(sample_size):
            l = [random.randint(0,48) for i in range(6)]
            if 2 in set([l.count(n) for n in l]):
                succ_tries += 1
        probability = succ_tries / sample_size
        return probability

lotto1 = Lotto(6)
lotto2 = lotto1

if lotto1.check(lotto2):
    print("yes")

print(f"{Lotto.calc_prob(100000) * 100}%")