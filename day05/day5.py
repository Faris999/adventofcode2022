with open('input.txt', 'r') as f:
    raw_input = f.read()

raw_stacks, instructions = (x.split('\n') for x in raw_input.split('\n\n'))

raw_stacks = raw_stacks[::-1]
num_stacks = int(raw_stacks[0].split(' ')[-2])
raw_stacks = raw_stacks[1:]

stacks = [list() for i in range(num_stacks)]

for row in raw_stacks:
    for i, j in enumerate(range(1, num_stacks*4, 4)):
        if row[j] != ' ':
            stacks[i].append(row[j])

for instruction in instructions:
    instruction = instruction.split(' ')
    quantity = int(instruction[1])
    src = int(instruction[3]) - 1
    dest = int(instruction[5]) - 1
    for i in range(quantity):
        stacks[dest].append(stacks[src].pop())

print(''.join([i[-1] for i in stacks]))

# Part 2
stacks = [list() for i in range(num_stacks)]

for row in raw_stacks:
    for i, j in enumerate(range(1, num_stacks*4, 4)):
        if row[j] != ' ':
            stacks[i].append(row[j])
for instruction in instructions:
    instruction = instruction.split(' ')
    quantity = int(instruction[1])
    src = int(instruction[3]) - 1
    dest = int(instruction[5]) - 1
    stacks[dest].extend(stacks[src][-quantity:])
    stacks[src] = stacks[src][:-quantity]


print(''.join([i[-1] for i in stacks]))