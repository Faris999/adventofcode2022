
with open('input.txt', 'r') as f:
    raw_input = f.read()

def sliding(x, n):
    return zip(*[x[i:] for i in range(n)])

for i, j in enumerate(sliding(raw_input, 4)):
    if len(set(j)) == 4:
        print(i+4)
        break
for i, j in enumerate(sliding(raw_input, 14)):
    if len(set(j)) == 14:
        print(i+14)
        break