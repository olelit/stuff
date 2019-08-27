import random
import time

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        left_element = left[0]
        right_element = right[0]
        result.append(
            left.pop(0)
            if left_element <= right_element 
            else right.pop(0)
            )
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    middle = int(len(numbers)/2)
    left = numbers[:middle]
    right = numbers[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)

    return result

numbers = [random.randint(0,100000) for _ in range(10000)]

start_time = time.time()
merge_sort(numbers)
print(time.time() - start_time)
