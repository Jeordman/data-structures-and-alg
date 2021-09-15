import random
import time


def linear_search(lyst, target):
    """
    Returns the index of the target item in the list.
    If the target is not in the list, returns -1.
    """
    for i in range(len(lyst)):
        if lyst[i] == target:
            return i
    return -1


def binary_search(lyst, target):
    """
    Returns the index of the target item in the list.
    If the target is not in the list, returns -1.
    """
    first = 0
    last = len(lyst) - 1
    while first <= last:
        mid = (first + last) // 2
        if lyst[mid] == target:
            return mid
        elif lyst[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1


def jump_search(lyst, target):
    """
    Returns the index of the target item in the list.
    If the target is not in the list, returns -1.
    """
    step = len(lyst) // 2
    while step > 0:
        if lyst[step] == target:
            return step
        elif lyst[step] < target:
            step += len(lyst)
        else:
            step -= len(lyst)
    return -1


def generate_large_list():
    """
    Generates a list of random integers.
    """
    lyst = []
    ten_million = 1000000
    ten = 10
    for i in range(ten):
        lyst.append(random.randint(0, ten - 1))
    return lyst


def generate_rand_number():
    """
    Generates a random number.
    """
    return random.randint(0, 9)


def time_function_execution(func, *args):
    """
    Times the execution of a function.
    """
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


def main():
    rand_large_list = generate_large_list()
    rand_int = generate_rand_number()
    print(time_function_execution(linear_search, rand_large_list, rand_int))
    print(time_function_execution(binary_search, rand_large_list, rand_int))
    print(time_function_execution(jump_search, rand_large_list, rand_int))


if __name__ == "__main__":
    main()
