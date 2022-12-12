with open('input.txt', 'r') as f:
    raw_input = f.read()

class Node():
    def __init__(self, pos, elevation, parent):
        self.pos = pos
        self.elevation = elevation
        self.parent = parent

    def __repr__(self) -> str:
        return f'{self.elevation}/{chr(ord("a")+self.elevation)} at {self.pos} parent={self.parent.pos if self.parent else None}'

def flip(x):
    return (x[1], x[0])

starting_pos = flip(divmod(raw_input.index('S'), raw_input.index('\n') + 1))
final_pos = flip(divmod(raw_input.index('E'), raw_input.index('\n') + 1))

clean_raw_input = raw_input.replace('S', 'a').replace('E', 'z')

matrix = [[ord(j) - ord('a') for j in i] for i in clean_raw_input.splitlines()]

WIDTH = len(matrix[0])
HEIGHT = len(matrix)

def get_neighbors(node, w, h):
    pos = node.pos
    neighbors = []
    if pos[0] != 0:
        neighbors.append((pos[0]-1, pos[1]))
    if pos[0] != w-1:
        neighbors.append((pos[0]+1, pos[1]))
    if pos[1] != 0:
        neighbors.append((pos[0], pos[1]-1))
    if pos[1] != h-1:
        neighbors.append((pos[0], pos[1]+1))
    return [Node(i, matrix[i[1]][i[0]], node) for i in neighbors]

frontier = []
visited = set()
current_node = Node(starting_pos, 0, None)
while True:
    if current_node.pos in visited:
        if len(frontier) == 0:
            break
        current_node = frontier.pop(0)
        continue
    neighbors = get_neighbors(current_node, WIDTH, HEIGHT)
    climbable_neighbors = [i for i in neighbors if current_node.elevation >= i.elevation - 1]
    frontier.extend(i for i in climbable_neighbors if i.pos not in visited)
    visited.add(current_node.pos)
    if len(frontier) == 0:
        break
    current_node = frontier.pop(0)
    if current_node.pos == final_pos:
        path_len = 0
        while current_node.parent is not None:
            current_node = current_node.parent
            path_len += 1
        print(path_len)
        break

# Part 2
def get_coords(n):
    return flip(divmod(n, raw_input.index('\n') + 1))
a_poses = [get_coords(i) for i, x in enumerate(clean_raw_input) if x == 'a']
print(a_poses)
path_lens = []
for starting_pos in a_poses:
    frontier = []
    visited = set()
    current_node = Node(starting_pos, 0, None)
    while True:
        if current_node.pos in visited:
            if len(frontier) == 0:
                break
            current_node = frontier.pop(0)
            continue
        neighbors = get_neighbors(current_node, WIDTH, HEIGHT)
        climbable_neighbors = [i for i in neighbors if current_node.elevation >= i.elevation - 1]
        frontier.extend(i for i in climbable_neighbors if i.pos not in visited)
        visited.add(current_node.pos)
        if len(frontier) == 0:
            break
        current_node = frontier.pop(0)
        if current_node.pos == final_pos:
            path_len = 0
            while current_node.parent is not None:
                current_node = current_node.parent
                path_len += 1
            path_lens.append(path_len)
            print(path_len)
            break

print(sorted(path_lens)[0])