# Part 1
with open('input.txt', 'r') as input:
    print (max([sum([int(x) for x in e.split('\n')]) for e in input.read().split('\n\n')]))

        
# Part 2
with open('input.txt', 'r') as input:
    print (sum(sorted([sum([int(x) for x in e.split('\n')]) for e in input.read().split('\n\n')], reverse=True)[:3]))
