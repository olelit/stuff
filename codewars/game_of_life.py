# -*- coding: utf-8 -*-
def get_cell_status(y, x, cells):
    output = 0
    count = 0

    for new_y in range(y-1,y+1):
        for new_x in range(x-1,x+1):
            if new_x > -1 and new_x < len(cells[new_y]) and new_y > -1 and new_y < len(cells) and (new_x != x and new_y != y):
                count += cells[new_y][new_x]

    if count < 2 or count > 3:
        output = 0
    elif count == 3:
        output = 1
    return output


def get_generation(cells, generations):
    new_cells = [[x for x in item] for item in cells]
    print("_________________")
    for generation in range(generations):
        for item_y in range(len(cells)):
            for item_x in range(len(cells[item_y])):
                new_cells[item_y][item_x] = get_cell_status(
                    item_y, item_x, cells)
    return new_cells

def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]
         
resp = get_generation(start, 1)

for item in resp:
    print("".join(map(str,item)))


#print(resp == end)
#print('Got<:LF:>' + htmlize(resp) + '<:LF:>instead of<:LF:>' + htmlize(end))

