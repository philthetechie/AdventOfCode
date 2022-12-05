import re

# Part 1
stack_array = [
    ['T','V','J','W','N','R','M','S'],
    ['V','C','P','Q','J','D','W','B'],
    ['P','R','D','H','F','J','B'],
    ['D','N','M','B','P','R','F'],
    ['B','T','P','R','V','H'],
    ['T','P','B','C'],
    ['L','P','R','J','B'],
    ['W','B','Z','T','L','S','C','N'],
    ['G','S','L']
]
reg = r"move (\d+) from (\d+) to (\d+)"

with open('input.txt', 'r') as input:
    for movement in input.read().split('\n'):
        number, start, end = map(int, (re.search(reg, movement).groups()))
        for n in range(0, number):
            t = stack_array[start-1][0]
            stack_array[start-1] = stack_array[start-1][1:]
            stack_array[end-1].insert(0, t)

print("".join([x[0] for x in stack_array]))


# Part 2
stack_array = [
    ['T','V','J','W','N','R','M','S'],
    ['V','C','P','Q','J','D','W','B'],
    ['P','R','D','H','F','J','B'],
    ['D','N','M','B','P','R','F'],
    ['B','T','P','R','V','H'],
    ['T','P','B','C'],
    ['L','P','R','J','B'],
    ['W','B','Z','T','L','S','C','N'],
    ['G','S','L']
]
reg = r"move (\d+) from (\d+) to (\d+)"

with open('input.txt', 'r') as input:
    for movement in input.read().split('\n'):
        number, start, end = map(int, (re.search(reg, movement).groups()))
        t = stack_array[start-1][0:number]
        stack_array[start-1] = stack_array[start-1][number:]
        stack_array[end-1] = t + stack_array[end-1]

print("".join([x[0] for x in stack_array]))