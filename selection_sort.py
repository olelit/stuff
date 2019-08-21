input_list = [
    70,
    43,
    1,
    2,
    87,
    122,
    876,
    4,
    4,
    5,
    56,
    23,
    67,
    345,
    78,
    23,
]


def find_minimum(input_list):
    min_index = 0
    for index in range(1, len(input_list)):
         min_index = index if input_list[index] < input_list[min_index] else min_index
    return min_index


sorted_list = []


for item in range(len(input_list)):
    minimum = find_minimum(input_list)
    sorted_list.append(input_list.pop(minimum))
print(sorted_list)




