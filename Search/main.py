import time

def naive_search(text_array, pattern):
    result = []

    text_width = len(text_array[0])
    text_height = len(text_array)

    pattern_width = max(len(pattern[i]) for i in range(len(pattern)))
    #length of longest line in pattern
    pattern_height = len(pattern)

    for y in range(text_height - pattern_height + 1):
        for x in range(text_width - pattern_width + 1):
            # 2D traversal of the array

            for i, line in enumerate(pattern):
                # starting from point (x,y) checking if text fragment matches pattern line by line

                if line != text_array[y + i][x:x+len(line)]:
                    break
                elif i == len(pattern) - 1:
                    # last line matches and hasn't broke yet - pattern must match

                    result.append((x, y))
    return result

def rabin_horizontal(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    result = []

    # pattern_hash = 0
    # for i in range(m):
    #     pattern_hash = (d * pattern_hash + ord(pattern[i])) % q

    for x in range(n - 2):
        p = 0
        t = 0

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[x][i])) % q
        for y in range(n - m + 1):
            if p == t:
                found = True
                for i in range(m):
                    if text[x][y + i] != pattern[i]:
                        found = False
                        break
                if found:
                    result.append((x,y))
            if y < n - m:
                t = ((t - h * ord(text[x][y])) * d + ord(text[x][y + m])) % q
    return result



def rabin_vertical(text, pattern, result):
    m = len(pattern)

    final_result = []

    for coordinate in result:
        text_string = ""
        for i in range(m):
            text_string += text[coordinate[0] + i][coordinate[1]]

        if text_string == pattern:
            final_result.append(coordinate)
    return final_result

def karp_search(text, pattern, d, q):
    hor_res = rabin_horizontal(text, pattern, d, q)
    return rabin_vertical(text, pattern, d, q, hor_res)

def test_case(naive_pattern, karp_pattern, array_sizes, alphabet):
    d = len(alphabet)
    result = []

    for test in array_sizes:
        f = open(f"patterns/{test}_pattern.txt")
        list = f.readlines()
        naive_start = time.time()
        naive_search(list, naive_pattern)
        naive_time = time.time() - naive_start

        karp_start = time.time()
        karp_search(list, karp_pattern, d, 17)
        karp_time = time.time() - karp_start
        result.append((round(naive_time, 2), round(karp_time, 2)))
        f.close()
    return result

if __name__ == "__main__":

    pattern = ["ABC",
               "B",
               "C"]
    test_pattern = "ABC"
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    test_sizes = ['1000', '2000', '3000', '4000', '5000', '8000']

    print(test_case(pattern, test_pattern, test_sizes, alphabet))
