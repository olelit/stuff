elements = [1, 2, 3, 4, 55, 8, 7, 45, 2, 5, 21, 4, 1, 2, 3]
count_element = {}

for item in elements:
    count_element[item] = count_element[item]+1 if item in count_element else 1

print(count_element)

