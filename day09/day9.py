with open('input.txt', 'r') as f:
    raw_input = f.read().splitlines()


visited = set()
head = (0, 0)
tail= (0, 0)

def move(position, direction, length=1):
    if direction == 'D':
        position = (position[0], position[1] - length)
    elif direction == 'U':
        position = (position[0], position[1] + length)
    elif direction == 'L':
        position = (position[0] - length, position[1])
    elif direction == 'R':
        position = (position[0] + length, position[1])
    return position

def is_touching(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def same_row_or_col(head, tail):
    return head[0] == tail[0] or head[1] == tail[1]

for line in raw_input:
    direction, length = line.split()
    length = int(length)
    for i in range(length):
        prev_head = head
        head = move(head, direction)
        if is_touching(head, tail):
            visited.add(tail)
            continue
        tail = prev_head
        # elif same_row_or_col(head, tail):
        #     tail = move(tail, direction)
        # else:
        #     tail = prev_head
        visited.add(tail)

print(len(visited))

# Part 2


def move_to(tail, head):
    x = tail
    if tail[0] < head[0]:
        x = move(x, 'R')
    elif tail[0] > head[0]:
        x = move(x, 'L')
    if tail[1] < head[1]:
        x = move(x, 'U')
    elif tail[1] > head[1]:
        x = move(x, 'D')
    return x

visited = set()
rope = [(0, 0) for i in range(10)]



for line in raw_input:
    direction, length = line.split()
    length = int(length)
    for i in range(length):
        prev = rope[0]
        rope[0] = move(rope[0], direction)
        for j in range(1, 10):
            if is_touching(rope[j-1], rope[j]):
                continue
            rope[j] = move_to(rope[j], rope[j-1])
        visited.add(rope[-1])
    
print(len(visited))