with open('input.txt', 'r') as f:
    raw_input = f.read().split('\n')

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for sack in raw_input:
    comp1 = set(sack[:len(sack)//2])
    comp2 = set(sack[len(sack)//2:])
    intersect = comp1.intersection(comp2)
    total += alphabet.index(list(intersect)[0]) + 1

print(total)

total = 0

for i in range(0, len(raw_input), 3):
    sack1 = set(raw_input[i])
    sack2 = set(raw_input[i+1])
    sack3 = set(raw_input[i+2])
    intersect = sack1.intersection(sack2).intersection(sack3)
    total += alphabet.index(list(intersect)[0]) + 1

print(total)

