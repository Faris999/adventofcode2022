from sympy import symbols, solve
import re

with open('input.txt', 'r') as f:
    raw_input = f.read()

variables = {i[0]: i[1] for i in [j.split(': ') for j in raw_input.splitlines()]}

root = variables['root']

while True:
    words = re.findall('[a-z]+', root)
    if len(words) == 0:
        break
    for word in words:
        root = root.replace(word, f'({variables[word]})')

print(eval(root))

# Part 2

raw_input = raw_input.replace('humn', 'x')

variables = {i[0]: i[1] for i in [j.split(': ') for j in raw_input.splitlines()]}
variables['x'] = 'x'

root = variables['root'].replace('+', '-')

while True:
    words = re.findall('[a-z]+', root) 
    if len(words) == 0:
        break
    if len(words) == 1 and words[0] == 'x':
        break
    for word in words:
        if word == 'x':
            continue
        root = root.replace(word, f'({variables[word]})')

x = symbols('x')
sol = solve(eval(root), x)
print(sol)