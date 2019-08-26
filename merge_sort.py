numbers = [12, 534, 4,5,213,12,4,3,65,65,767,9,4,53,5,232,2,34,5,6,6,56,5,9, 12, 44, 3, 1, 3, 5, 7, 8, 5, 4, 23, 1, 87, 54, 1092]

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        result.append(max(left.pop(), right.pop()))

        result.append([item for item in left if len(left) > 0 ])
        result.append([item for item in right if len(right) > 0])

    return result

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    left = [item for item in numbers[:int(len(numbers)/2)]]
    right = [item for item in numbers[int((len(numbers)/2)):]]

    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left, right)

    return result

print(merge_sort(numbers))
