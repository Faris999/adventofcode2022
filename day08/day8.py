with open('input.txt', 'r') as f:
    raw_input = f.read().splitlines()

grid = [[int(i) for i in line] for line in raw_input]

visible = set()
grid_size = (len(grid), len(grid[0]))


# Left to right
for i, row in enumerate(grid):
    current_highest = -1
    for j, tree in enumerate(row):
        if tree > current_highest:
            current_highest = tree
            visible.add((i, j))

# Right to left
for i, row in enumerate(grid):
    current_highest = -1
    for j, tree in enumerate(row[::-1]):
        if tree > current_highest:
            current_highest = tree
            visible.add((i, grid_size[1] - j - 1))

# top to bottom
transposed = list(map(list, zip(*grid)))
for i, col in enumerate(transposed):
    current_highest = -1
    for j, tree in enumerate(col):
        if tree > current_highest:
            current_highest = tree
            visible.add((j, i))

# bottom to top
for i, col in enumerate(transposed):
    current_highest = -1
    for j, tree in enumerate(col[::-1]):
        if tree > current_highest:
            current_highest = tree
            visible.add((grid_size[0] - j - 1, i))

print(sorted(list(visible)))
print(len(visible))

# Part 2

max_scenic_score = 0

for i, row in enumerate(grid):
    if i == 0 or i == grid_size[0]-1:
        continue

    for j, tree in enumerate(row):
        if j == 0 or j == grid_size[1]-1:
            continue
        
        scenic_score = 1



        up = 0
        current_pos = (i, j)
        while True:
            current_pos = (current_pos[0] - 1, current_pos[1])
            if current_pos[0] < 0:
                break
            up += 1
            if grid[current_pos[0]][current_pos[1]] >= tree:
                break

        down = 0
        current_pos = (i, j)
        while True:
            current_pos = (current_pos[0] + 1, current_pos[1])
            if current_pos[0] >= grid_size[0]:
                break
            down += 1
            if grid[current_pos[0]][current_pos[1]] >= tree:
                break

        left = 0
        current_pos = (i, j)
        while True:
            current_pos = (current_pos[0], current_pos[1] - 1)
            if current_pos[1] < 0:
                break
            left += 1
            if grid[current_pos[0]][current_pos[1]] >= tree:
                break

        right = 0
        current_pos = (i, j)
        while True:
            current_pos = (current_pos[0], current_pos[1] + 1)
            if current_pos[1] >= grid_size[1]:
                break
            right += 1
            if grid[current_pos[0]][current_pos[1]] >= tree:
                break

        scenic_score = up * down * left * right
        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)

            