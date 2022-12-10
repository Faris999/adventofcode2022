with open('input.txt', 'r') as f:
    raw_input = f.read().splitlines()

cycle = 1
x = 1
to_add = None
ops = iter(raw_input)
total = 0
current_op = None

while True:
    try:
        if current_op is None:
            op = next(ops)
    except StopIteration:
        break
    if to_add is not None:
        x += to_add
        to_add = None
        current_op = None
    elif op.startswith('addx'):
        to_add = int(op.split()[1])
        current_op = 'addx'
    cycle += 1
    if (cycle - 20) % 40 == 0:
        total += cycle * x

print(total)

# Part 2
cycle = 1
x = 1
to_add = None
ops = iter(raw_input)
current_op = None

while True:
    try:
        if current_op is None:
            op = next(ops)
    except StopIteration:
        break
    if abs((cycle % 40) - x -1) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if to_add is not None:
        x += to_add
        to_add = None
        current_op = None
    elif op.startswith('addx'):
        to_add = int(op.split()[1])
        current_op = 'addx' 
    cycle += 1
    if (cycle - 1) % 40 == 0:
        print()