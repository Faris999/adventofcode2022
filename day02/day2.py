with open('input.txt', 'r') as f:
    raw_input = f.read().split('\n')

# Part 1

score_dict = {
    'A X' : 3 + 1,
    'A Y' : 6 + 2,
    'A Z' : 0 + 3,
    'B X' : 0 + 1,
    'B Y' : 3 + 2,
    'B Z' : 6 + 3,
    'C X' : 6 + 1,
    'C Y' : 0 + 2,
    'C Z' : 3 + 3,
    '' : 0
}

print(sum(score_dict[i] for i in raw_input))

# Part 2

score_dict = {
    'A X' : 0 + 3,
    'A Y' : 3 + 1,
    'A Z' : 6 + 2,
    'B X' : 0 + 1,
    'B Y' : 3 + 2,
    'B Z' : 6 + 3,
    'C X' : 0 + 2,
    'C Y' : 3 + 3,
    'C Z' : 6 + 1,
    '' : 0
}


print(sum(score_dict[i] for i in raw_input))