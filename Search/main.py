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

    pattern_hash = 0
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q

    for line_index in range(n - 2):
        text_hash = 0
        for b in range(m):
            text_hash = (d * text_hash + ord(text[line_index][b])) % q
        for s in range(n - m):
            if text_hash == pattern_hash:
                if pattern == text[line_index][s:s+m]:
                    result.append((line_index, s))
            text_hash = (d * (text_hash - ord(text[line_index][s]) * h) + ord(text[line_index][s + m])) % q
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
    return rabin_vertical(text, pattern, hor_res)

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
        print(f"done iteration with data size: {test}")
    return result

if __name__ == "__main__":

    pattern = ["ABC",
               "B",
               "C"]
    test_pattern = "ABC"
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    test_sizes = ['1000', '2000', '3000', '4000', '5000', '8000']

    print(test_case(pattern, test_pattern, test_sizes, alphabet))

    # f = open("patterns/1000_pattern.txt")
    # line = f.readlines()

    #print(karp_search(line, test_pattern, 16, 17))
