
def naive_search(text_array, pattern):
    occ_count = 0
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

                    occ_count += 1
                    print(f"found on x,y: {x, y}")
    return occ_count

if __name__ == "__main__":

    pattern = ["ABC",
               "B",
               "C"]

    f = open('patterns/1000_pattern.txt')
    list1 = f.readlines()
    print(naive_search(list1, pattern))

