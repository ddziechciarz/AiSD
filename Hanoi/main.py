

def hanoi_rec(size, start, end):
    move_count = 0
    if size <= 1:
        print(f"{start} -> {end}")
        return move_count + 1
    else:
        other = 6 - (start + end)
        move_count += hanoi_rec(size - 1, start, other)
        print(f"{start} -> {end}")
        move_count += 1
        move_count += hanoi_rec(size - 1, other, end)
        return move_count

# def make_move(start_stack, end_stack):
#     end_stack.append(start_stack.pop)


def hanoi_iter(size):
    i = 1
    stack_start = [i + 1 for i in range(size)]
    stack_help = []
    stack_end = []

    if stack_start[-1] % 2 == 0:
        is_even = True
    else:
        is_even = False

    while stack_start or stack_help:
        if (i % 3 == 1 and not is_even) or (i % 3 == 2 and is_even):
            #print(f"start_stack: {stack_start}, end_stack: {stack_end}")
            #possible move between start and end
            if len(stack_start) != 0 and (len(stack_end) == 0 or stack_start[-1] > stack_end[-1]):
                print("1 -> 3")
                i += 1
                stack_end.append(stack_start.pop())
            else:
                print("3 -> 1")
                stack_start.append(stack_end.pop())
                i += 1

        elif (i % 3 == 2 and not is_even) or (i % 3 == 1 and is_even):
            #print(f"start_stack: {stack_start}, help_stack: {stack_help}")
            #possible move between start and help
            if len(stack_start) != 0 and (len(stack_help) == 0 or stack_start[-1] > stack_help[-1]):
                print("1 -> 2")
                stack_help.append(stack_start.pop())
                i += 1
            else:
                print("2 -> 1")
                stack_start.append(stack_help.pop())
                i += 1

        elif i % 3 == 0:
            #print(f"help_stack: {stack_help}, end_stack: {stack_end}")
            #possbile move between help and end
            if len(stack_help) != 0 and (len(stack_end) == 0 or stack_help[-1] > stack_end[-1]):
                print("2 -> 3")
                stack_end.append(stack_help.pop())
                i += 1
            else:
                print("3 -> 2")
                stack_help.append(stack_end.pop())
                i += 1

    return i - 1


iteration_moves = hanoi_iter(15)
recursion_moves = hanoi_rec(15, 1, 3)

print(iteration_moves, recursion_moves)