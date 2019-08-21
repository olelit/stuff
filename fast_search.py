
numbers = [3,4]


def rec_search(numbers, summ = 0):
    if len(numbers) == 0:
        return summ
    index = numbers.pop()
    summ += index
    return rec_search(numbers,summ)



print(rec_search(numbers))
