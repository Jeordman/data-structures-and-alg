import time
import random


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


def is_sorted(array):
    return all(array[i] <= array[i+1] for i in range(len(array)-1))


def generate_large_array():
    return [random.randint(0, 100) for _ in range(10000)]


def time_function_execution(func, *args):
    print('starting ' + func.__name__)
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    time_elapsed = end - start
    print(func.__name__ + ' duration: ' + str(time_elapsed))
    return time_elapsed


def main():
    time_function_execution(quick_sort, generate_large_array())
    time_function_execution(merge_sort, generate_large_array())
    time_function_execution(selection_sort, generate_large_array())
    time_function_execution(insertion_sort, generate_large_array())
    time_function_execution(list.sort, generate_large_array())


main()
