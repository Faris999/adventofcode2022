with open('input.txt', 'r', encoding='utf-8') as f:
    raw_input = f.read()


# Part 1

elves = raw_input.split('\n\n')
largest = 0
for elf in elves:
    value = sum(int(i) for i in elf.split('\n'))
    if value > largest:
        largest = value

print(largest)

# Part 2

elves = raw_input.split('\n\n')
elves = [sum(int(i) for i in elf.split('\n')) for elf in elves]

print(sum(sorted(elves)[-3:]))