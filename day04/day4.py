with open('input.txt', 'r') as f:
    raw_input = f.read().split('\n')

total = 0
total2 = 0

for i in raw_input:
    elf1, elf2 = tuple(i.split(','))
    l1, u1 = tuple(int(i) for i in elf1.split('-'))
    l2, u2 = tuple(int(i) for i in elf2.split('-'))
    if i == '6-47,5-5':
        print('a')
    if (l1 >= l2 and u1 <= u2) or (l2 >= l1 and u2 <= u1):
        total += 1
        # print(i, l1, u1, l2, u2)
    else:
        print('a')
    if (u1 >= l2 and l1 <= l2) or (u2 >= l1 and l2 <= l1):
        print(i)
        total2 += 1

pairs = []
for line in raw_input:
    # Split the line on the comma and convert each range into a tuple
    ranges = [tuple(map(int, range.split("-"))) for range in line.split(",")]
    pairs.append(ranges)

# Initialize a counter for the number of pairs that need reconsideration
counter = 0

# Iterate over each pair of ranges
for pair in pairs:
    # Unpack the pair of ranges
    range1, range2 = pair

    # Check if one range fully contains the other
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        counter += 1
    elif range2[0] <= range1[0] and range2[1] >= range1[1]:
        counter += 1

# Return the counter as the result
print(counter)

pairs = []
for line in raw_input:
    # Split the line on the comma and convert each range into a tuple
    ranges = [tuple(map(int, range.split("-"))) for range in line.split(",")]
    pairs.append(ranges)

# Initialize a counter for the number of pairs that overlap
counter = 0

# Iterate over each pair of ranges
for pair in pairs:
    # Unpack the pair of ranges
    range1, range2 = pair

    # Check if the ranges overlap
    if range1[1] >= range2[0] and range1[0] <= range2[1]:
        counter += 1

print(counter)

print(total)
print(total2)