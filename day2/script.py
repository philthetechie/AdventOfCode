# part 1
game_vars = {
    "X": {'map': 'A', 'score': 1, 'win': "C"},
    "Y": {'map': 'B', 'score': 2, 'win': "A"},
    "Z": {'map': 'C', 'score': 3, 'win': "B"},
}

points = 0
with open('input.txt', 'r') as input:
    for game in input.read().split('\n'):
        them, us = game.split(" ")
        us = us.strip()
        them = them.strip()
        if them == game_vars[us]['map']:
            points += (game_vars[us]['score'] + 3)
            continue
        points += (game_vars[us]['score'] + 6) if game_vars[us]['win'] == them else game_vars[us]['score']

print (points)


# part 2
wins = {  # w     # L      # d
    "A": {'Z':2, 'X': 3, 'Y':1 }, # rock
    "B": {'Z':3, 'X': 1, 'Y':2 }, # paper
    "C": {'Z':1, 'X': 2, 'Y':3 }, # scissors
}
bonus = {'Z':6, 'X':0, 'Y':3 }
points = 0
with open('input.txt', 'r') as input:
    for game in input.read().split('\n'):
        them, outcome = game.split(" ")
        points += wins[them][outcome] + bonus[outcome]
    
print (points)

