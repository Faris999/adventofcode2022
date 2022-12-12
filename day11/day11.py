from typing import List


class Monkey():
    def __init__(self, items, operation, predicate, dst_true, dst_false):
        self.items = items
        self.operation = operation
        self.predicate = predicate
        self.dst_true = dst_true
        self.dst_false = dst_false
        self.num_inspections = 0

with open('input.txt', 'r') as f:
    raw_input = f.read()



raw_monkeys = raw_input.split('\n\n')

monkeys = []


# Parsing

for raw_monkey in raw_monkeys:
    _, items, operation, predicate, dst_true, dst_false = raw_monkey.split('\n')
    items = [int(i) for i in items.split(':')[1].split(',')]
    operation = eval(f'lambda old: {operation.split("=")[1]}')
    div_by = int(predicate.rsplit(' ', 1)[1])
    print(div_by)
    predicate = (lambda y: lambda x: x % y == 0)(div_by)
    dst_true = int(dst_true.rsplit(' ', 1)[1])
    dst_false = int(dst_false.rsplit(' ', 1)[1])
    monkey = Monkey(items, operation, predicate, dst_true, dst_false)
    monkeys.append(monkey)

for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            item = monkey.operation(item)
            monkey.num_inspections += 1
            item = item // 3
            dst = monkey.dst_true if monkey.predicate(item) else monkey.dst_false
            monkeys[dst].items.append(item)
        monkey.items = list()

inspections = list(monkey.num_inspections for monkey in monkeys)
print(inspections)
inspections.sort(reverse=True)

print(inspections[0] * inspections[1])

# Part 2

monkeys = []


# Parsing

remainders_prod = 1

for raw_monkey in raw_monkeys:
    _, items, operation, predicate, dst_true, dst_false = raw_monkey.split('\n')
    items = [int(i) for i in items.split(':')[1].split(',')]
    operation = eval(f'lambda old: {operation.split("=")[1]}')
    div_by = int(predicate.rsplit(' ', 1)[1])
    remainders_prod *= div_by
    predicate = (lambda y: lambda x: x % y == 0)(div_by)
    dst_true = int(dst_true.rsplit(' ', 1)[1])
    dst_false = int(dst_false.rsplit(' ', 1)[1])
    monkey = Monkey(items, operation, predicate, dst_true, dst_false)
    monkeys.append(monkey)

for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            item = monkey.operation(item)
            item %= remainders_prod 
            monkey.num_inspections += 1
            dst = monkey.dst_true if monkey.predicate(item) else monkey.dst_false
            monkeys[dst].items.append(item)
        monkey.items = list()

inspections = list(monkey.num_inspections for monkey in monkeys)
print(inspections)
inspections.sort(reverse=True)

print(inspections[0] * inspections[1])