# Part 1

total = 0
lowercase_modifier = -96
uppercase_modifier = -38

with open('input.txt', 'r') as input:
    for bag in input.read().split('\n'):
        dupes = set(list(bag[:len(bag)//2])) & set(list(bag[len(bag)//2:]))
        total += sum([ord(x) + (uppercase_modifier if x.isupper() else lowercase_modifier) for x in list(dupes)])
print (total)

# part 2
total = 0
lowercase_modifier = -96
uppercase_modifier = -38
import numpy as np

with open('input.txt', 'r') as input:
    bags = input.read().split('\n')
    for group in np.array_split(bags, len(bags) / 3):
        badge = set(group[0]) & set(group[1]) & set(group[2])
        total += sum([ord(x) + (uppercase_modifier if x.isupper() else lowercase_modifier) for x in list(badge)])
print (total)
