import re

# Part 1
stack_array = []
reg = r"\[(.+)\]\ ?"
with open('input.txt', 'r') as input:
    state, input_data = input.read().split('\n\n')
    state = state.split('\n')[:-1]
    state = state[::-1]
    for line in state:
        for index, chunk in enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
            try: 
                stack_array[index]
            except:
                stack_array.append([])

            box = re.search(reg, chunk)
            if box:
                stack_array[index].append(box.groups()[0])
    stack_array = [x[::-1] for x in stack_array]
reg = r"move (\d+) from (\d+) to (\d+)"

for movement in input_data.split('\n'):
    number, start, end = map(int, (re.search(reg, movement).groups()))
    for n in range(0, number):
        t = stack_array[start-1][0]
        stack_array[start-1] = stack_array[start-1][1:]
        stack_array[end-1].insert(0, t)

print("".join([x[0] for x in stack_array]))


# Part 2
stack_array = []
reg = r"\[(.+)\]\ ?"
with open('input.txt', 'r') as input:
    state, input_data = input.read().split('\n\n')
    state = state.split('\n')[:-1]
    state = state[::-1]
    for line in state:
        for index, chunk in enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
            try: 
                stack_array[index]
            except:
                stack_array.append([])

            box = re.search(reg, chunk)
            if box:
                stack_array[index].append(box.groups()[0])
    stack_array = [x[::-1] for x in stack_array]
reg = r"move (\d+) from (\d+) to (\d+)"

for movement in input_data.split('\n'):
    number, start, end = map(int, (re.search(reg, movement).groups()))
    t = stack_array[start-1][0:number]
    stack_array[start-1] = stack_array[start-1][number:]
    stack_array[end-1] = t + stack_array[end-1]

print("".join([x[0] for x in stack_array]))