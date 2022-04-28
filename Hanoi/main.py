# def hanoi_rec(size, start, end):
#     move_count = 0
#     if size <= 1:
#         print(f"{start} -> {end}")
#         return move_count + 1
#     else:
#         other = 6 - (start + end)
#         move_count += hanoi_rec(size - 1, start, other)
#         print(f"{start} -> {end}")
#         move_count += 1
#         move_count += hanoi_rec(size - 1, other, end)
#         return move_count

def hanoi_recursion(size, start, buffer, end):
    move_count = 0
    if size <= 1:
        end.append(start.pop)
        return move_count + 1
    else:
        move_count += hanoi_recursion(size - 1, start, end, buffer)
        end.append(start.pop)
        move_count += 1
        move_count += hanoi_recursion(size - 1, buffer, start, end)
        return move_count


def hanoi_iter(size, start_stack:list, help_stack:list, end_stack:list, print_moves=False):
    i = 1
    stack_start = start_stack
    stack_help = help_stack
    stack_end = end_stack

    if stack_start[-1] % 2 == 0:
        is_even = True
    else:
        is_even = False

    while stack_start or stack_help:
        if (i % 3 == 1 and not is_even) or (i % 3 == 2 and is_even):
            #print(f"start_stack: {stack_start}, end_stack: {stack_end}")
            #possible move between start and end
            if len(stack_start) != 0 and (len(stack_end) == 0 or stack_start[-1] > stack_end[-1]):
                if print_moves:
                    print("1 -> 3")
                i += 1
                stack_end.append(stack_start.pop())
            else:
                if print_moves:
                    print("3 -> 1")
                stack_start.append(stack_end.pop())
                i += 1

        elif (i % 3 == 2 and not is_even) or (i % 3 == 1 and is_even):
            #print(f"start_stack: {stack_start}, help_stack: {stack_help}")
            #possible move between start and help
            if len(stack_start) != 0 and (len(stack_help) == 0 or stack_start[-1] > stack_help[-1]):
                if print_moves:
                    print("1 -> 2")
                stack_help.append(stack_start.pop())
                i += 1
            else:
                if print_moves:
                    print("2 -> 1")
                stack_start.append(stack_help.pop())
                i += 1

        elif i % 3 == 0:
            #print(f"help_stack: {stack_help}, end_stack: {stack_end}")
            #possbile move between help and end
            if len(stack_help) != 0 and (len(stack_end) == 0 or stack_help[-1] > stack_end[-1]):
                if print_moves:
                    print("2 -> 3")
                stack_end.append(stack_help.pop())
                i += 1
            else:
                if print_moves:
                    print("3 -> 2")
                stack_help.append(stack_end.pop())
                i += 1

    return i - 1


def calc(sample_size):
    time_dict = {}
    for i in range(1, sample_size + 1):
        print(i)
        stack_start = [b for b in range(1, i + 1)]
        stack_buffer = []
        stack_end = []
        time_dict[f"{i}"] = (hanoi_iter(i, stack_start, stack_buffer, stack_end),
                             hanoi_recursion(i, stack_start, stack_buffer, stack_end))

    return time_dict
if __name__ == "__main__":
    print(calc(20))


