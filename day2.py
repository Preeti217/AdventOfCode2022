import os

path = "/Users/preetinarayanan/Desktop/AdventOfCode"
os.chdir(path)

rock_selected = 1
paper_selected = 2
scissors_selected = 3

# A - opponent plays rock
# B = opponent plays paper
# C = opponent plays scissors
#
# X - player plays rock
# Y - player plays paper
# Z - player plays scissors

#create dict for opponent and self(player)
self = {'X':1,'Y':2,'Z':3}
draw = 3
win = 6
def get_score(r):
    opponent_move = r[0]
    self_move = r[1]
    if self_move == 'X':
        score = self['X']
        if opponent_move == 'A':
            return score+draw
        elif opponent_move == 'B':
            return score
        else: return score+win
    elif self_move == 'Y':
        score = self['Y']
        if opponent_move == 'A':
            return score+win
        elif opponent_move == 'B':
            return score+draw
        else: return score
    else:
        score = self['Z']
        if opponent_move == 'A':
            return score
        elif opponent_move == 'B':
            return score+win
        else: return score+draw


#####Part two
def get_strategy(r):
    opponent_move = r[0]
    self_strategy = r[1]

    if self_strategy == 'X':
        if opponent_move == 'A': return self['Z']
        elif opponent_move == 'B': return self['X']
        else: return self['Y']
    elif self_strategy == 'Z':
        if opponent_move == 'A': return self['Y'] + 6
        elif opponent_move == 'B': return self['Z'] + 6
        else: return self['X'] + 6
    else:
        if opponent_move == 'A': return self['X'] + 3
        elif opponent_move == 'B': return self['Y'] + 3
        else: return self['Z'] + 3

file_name = 'day2.txt'

with open(file_name) as f:
    lines = f.readlines()

final_score = 0
for line in lines:
    game_round = line.split()
    #final_score += get_score(game_round)
    final_score += get_strategy(game_round)

print(final_score)