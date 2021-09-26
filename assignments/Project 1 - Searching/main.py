import random
import math
import time

random.seed(10)
ALLOWED_NUMBERS = 10000000
LIST_LENGTH = 1000000


def linear_search(lyst, target):
    for i in range(len(lyst)):
        if lyst[i] == target:
            return True
    return False


def recursive_binary_search(lyst, target):
    if len(lyst) == 0:
        return False
    else:
        mid = len(lyst) // 2
        if lyst[mid] == target:
            return True
        elif lyst[mid] < target:
            return recursive_binary_search(lyst[mid + 1:], target)
        else:
            return recursive_binary_search(lyst[:mid], target)


def jump_search(lyst, target):
    # https: // www.codespeedy.com/jump-search-algorithm-in-python/
    gap = math.sqrt(len(lyst))
    left = 0
    while(lyst[int(min(gap, len(lyst))-1)] < target):
        left = gap
        gap = gap + math.sqrt(len(lyst))
        if(left >= len(lyst)):
            break
    while(lyst[int(left)] < target):
        left = left + 1
        if(left == min(gap, len(lyst))):
            break
    if(lyst[int(left)] == target):
        return True
    return False


def get_large_list():
    return random.sample(range(ALLOWED_NUMBERS), k=LIST_LENGTH)


def time_function_execution(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


def get_test_numbers(lyst):
    first_item = lyst[0]
    middle_item = lyst[len(lyst) // 2]
    last_item = lyst[len(lyst) - 1]
    unfindable_item = -1
    return [first_item, middle_item, last_item, unfindable_item]


def apply_funtion_repeatedly(testNums, func, randLargeList):
    print(func.__name__)
    for i in testNums:
        print(time_function_execution(func, randLargeList, i))


def main():
    randLargeList = get_large_list()
    testNums = get_test_numbers(randLargeList)
    apply_funtion_repeatedly(testNums, linear_search, randLargeList)
    apply_funtion_repeatedly(testNums, recursive_binary_search, randLargeList)
    apply_funtion_repeatedly(testNums, jump_search, randLargeList)


if __name__ == "__main__":
    main()
