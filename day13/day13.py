from functools import cmp_to_key

with open('input.txt', 'r') as f:
    raw_input = f.read()

pairs = [tuple(eval(j) for j in i.splitlines()) for i in raw_input.split('\n\n')]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: 
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return None
        if len(left) == 0:
            return True
        elif len(right) == 0:
            return False
        comparison = compare(left.pop(0), right.pop(0))
        if comparison is not None:
            return comparison
        return compare(left, right)
    else:
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return compare(left, right)

total = 0

for i, pair in enumerate(pairs):
    result = compare(pair[0], pair[1])
    if result:
        total += i + 1

print(total)

# part 2
def compare2(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: 
            return 1
        elif left > right:
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) == 0:
            return 0
        if len(left) == 0:
            return 1
        elif len(right) == 0:
            return -1
        comparison = compare2(left[0], right[0])
        if comparison != 0:
            return comparison
        return compare2(left[1:], right[1:])
    else:
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return compare2(left, right)

packets = [eval(i) for i in raw_input.replace('\n\n', '\n').splitlines()] + [[[2]], [[6]]]
# packets = [[1], [2]]

packets = sorted(packets, key=cmp_to_key(compare2), reverse=True)

decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(packets)
print(decoder_key)
