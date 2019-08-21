def binary_search(find, numbers, start, end,steps):

    mid = int((start+end)/2)

    if numbers[mid] == find:
        return mid,steps
    
    start = mid if numbers[mid] < find else start
    end = mid if numbers[mid] > find else end

    steps+=1

    return binary_search(find, numbers, start, end, steps)
    

numbers = []

find = 543123

for i in range(1000000):
    numbers.append(i)

position,steps = binary_search(find, numbers, 0, len(numbers), 0)

print(position)
print(steps)
