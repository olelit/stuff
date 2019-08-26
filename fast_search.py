numbers = [12,534,12,44,3,1,3,5,7,8,5,4,23,1,87,54,1092]

def quick_search(value):
    if len(value) < 2:
        return value
    base = value[int(len(value)/2)]
    smaller = [item for item in value if item < base]
    bigger = [item for item in value if item > base]
    equal = [item for item in value if item == base]
    return quick_search(smaller) + equal + [base] + quick_search(bigger)

print(quick_search(numbers))
