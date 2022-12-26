with open('input.txt', 'r') as f:
    raw_input = f.read()

snafu_dict = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}

def snafu_to_dec(s):
    s = s[::-1]
    return sum(snafu_dict[digit] * (5**i) for i, digit in enumerate(s))

def dec_to_base5(s):
    dec = int(s)
    if dec == 0:
        return '0'
    digits = []
    while dec:
        digits.append(str(dec % 5))
        dec //= 5
    return ''.join(digits[::-1])

def base5_to_snafu(s):
    s = list(s[::-1])
    s.append('0')
    replacement = {'3': '=', '4': '-'}
    for i in range(len(s)-1):
        digit = s[i]
        s[i] = replacement.get(digit, digit)
        if digit in replacement:
            s[i+1] = str(int(s[i+1]) + 1)
        if s[i+1] == '5':
            s[i+1] = '4'
            remaining = s[:i:-1]
            x = int(''.join(remaining).lstrip('0'), base=5) + 1
            s = s[:i+1] + list(dec_to_base5(x)[::-1]) + ['0']

    return ''.join(s[::-1]).lstrip('0')

def dec_to_snafu(x):
    return base5_to_snafu(dec_to_base5(x))

total = 0
for line in raw_input.splitlines():
    total += snafu_to_dec(line)
print(dec_to_snafu((total)))