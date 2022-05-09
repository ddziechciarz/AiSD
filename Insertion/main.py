import random
import time

def insertionsort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x


def merge(A, start, mid, end):
    helper = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if A[i] <= A[j]:
            helper.append(A[i])
            i += 1
        else:
            helper.append(A[j])
            j += 1

    while i <= mid:
        helper.append(A[i])
        i += 1

    while j <= end:
        helper.append(A[j])
        j += 1

    for i in range(start, end + 1):
        A[i] = helper[i - start]


def mergesort(A, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(A, start, mid)
        mergesort(A, mid + 1, end)
        merge(A, start, mid, end)


if __name__ == '__main__':
    num_of_iterations = 20
    len_of_array = 10000

    insertion_times, merge_times = [], []

    for x in range(num_of_iterations):
        tab_to_sort_1 = [random.randint(0, 1000) for i in range(len_of_array)]
        tab_to_sort_2 = tab_to_sort_1

        start_time = time.time()
        insertionsort(tab_to_sort_1)
        insertion_times.append(time.time() - start_time)

        start_time = time.time()
        mergesort(tab_to_sort_2, 0, len(tab_to_sort_2) - 1)
        merge_times.append(time.time() - start_time)

        print(f"Iteration {x + 1} done")

    print(f"Shortest insertion sort time: {min(insertion_times)}, "
          f"Longest insertion sort time: {max(insertion_times)}, "
          f"Mean insertion sort time: {sum(insertion_times) / len(insertion_times)}, "
          f"for {num_of_iterations} iterations of {len_of_array} array length")

    print(f"Shortest merge sort time: {min(merge_times)}, "
          f"Longest merge sort time: {max(merge_times)}, "
          f"Mean merge sort time: {sum(merge_times) / len(merge_times)}, "
          f"for {num_of_iterations} iterations of {len_of_array} array length")
