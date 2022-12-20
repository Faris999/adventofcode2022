with open('input.txt', 'r') as f:
    raw_input = f.read()

encrypted = [int(i) for i in raw_input.splitlines()]

decrypted = encrypted.copy()

length = len(encrypted)

for i, num in enumerate(encrypted):
    old_pos = decrypted.index(num)
    new_pos = (num + old_pos) % (length-1)
    decrypted = decrypted[:old_pos] + decrypted[old_pos+1:]
    if new_pos == 0:
        decrypted.append(num)
    else:
        decrypted.insert(new_pos, num)

zero_pos = decrypted.index(0)
print(decrypted[(zero_pos+1000)%length])
print(decrypted[(zero_pos+2000)%length])
print(decrypted[(zero_pos+3000)%length])
grove_sum = decrypted[(zero_pos+1000)%length] + decrypted[(zero_pos+2000)%length] + decrypted[(zero_pos+3000)%length]
print(grove_sum)