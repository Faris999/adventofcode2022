with open('input.txt', 'r') as f:
    raw_input = f.read()

objects = {}

def get_path(p1, p2):
    '''Assumes the line specified by points are parallel with the x or y axis'''
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        return [(x1, y) for y in range(y_min, y_max+1)]
    
    if y1 == y2:
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        return [(x, y1) for x in range(x_min, x_max+1)]

max_y = 0

for path in raw_input.splitlines():
    points = [tuple(int(j) for j in i.split(',')) for i in path.split(' -> ')]
    max_y = max(max_y, *[i[1] for i in points])
    for p1, p2 in zip(points, points[1:]):
        for i in get_path(p1, p2):
            objects[i] = '#'


current_sand = (500,0)
objects[current_sand] = 'o'

def move_sand(sand, objects: dict):
    x, y = sand
    if objects.get((x, y+1), '.') == '.':
        return (x, y+1)
    if objects.get((x-1, y+1), '.') == '.':
        return (x-1, y+1)
    if objects.get((x+1, y+1), '.') == '.':
        return (x+1, y+1)
    return sand

num_sand = 0

while True:
    new_pos = move_sand(current_sand, objects)
    if new_pos == current_sand:
        current_sand = (500,0)
        num_sand += 1
        continue
    if new_pos[1] >= max_y:
        break
    objects[current_sand] = '.'
    objects[new_pos] = 'o'
    current_sand = new_pos

print(num_sand)

# Part 2

max_y = 0
min_x = 99999
max_x = 0
objects = {}

for path in raw_input.splitlines():
    points = [tuple(int(j) for j in i.split(',')) for i in path.split(' -> ')]
    max_y = max(max_y, *[i[1] for i in points])
    min_x = min(min_x, *[i[0] for i in points])
    max_x = max(max_x, *[i[0] for i in points])
    for p1, p2 in zip(points, points[1:]):
        for i in get_path(p1, p2):
            objects[i] = '#'

for i in range(min_x - 500, max_x + 500):
    objects[(i, max_y + 2)] = '#'

def move_sand(sand, objects: dict):
    x, y = sand
    if objects.get((x, y+1), '.') == '.':
        return (x, y+1)
    if objects.get((x-1, y+1), '.') == '.':
        return (x-1, y+1)
    if objects.get((x+1, y+1), '.') == '.':
        return (x+1, y+1)
    return sand

num_sand = 1
current_sand = (500,0)
objects[current_sand] = 'o'

while True:
    new_pos = move_sand(current_sand, objects)
    if new_pos == (500,0):
        break
    if new_pos == current_sand:
        current_sand = (500,0)
        num_sand += 1
        print(num_sand)
        if num_sand == 64:
            pass
        continue
    objects[current_sand] = '.'
    objects[new_pos] = 'o'
    current_sand = new_pos

print(num_sand)
