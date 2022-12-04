# Part 1

total = 0

with open('input.txt', 'r') as input:
    for section in input.read().split('\n'):
        t1, t2 = section.split(',')
        t1 = set(range(int(t1.split('-')[0]), int(t1.split('-')[1]) + 1))
        t2 = set(range(int(t2.split('-')[0]), int(t2.split('-')[1]) + 1))
        iscontained = True if t1.issubset(t2) or t1.issuperset(t2) else False
        if iscontained:
            total += 1
print (total)

# Part 1

total = 0

with open('input.txt', 'r') as input:
    for section in input.read().split('\n'):
        t1, t2 = section.split(',')
        t1 = set(range(int(t1.split('-')[0]), int(t1.split('-')[1]) + 1))
        t2 = set(range(int(t2.split('-')[0]), int(t2.split('-')[1]) + 1))
        iscontained = True if t1 & t2 else False
        if iscontained:
            total += 1
print (total)
