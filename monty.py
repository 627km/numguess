from random import shuffle, choice

change_for_success = 0
nochange_for_success = 0
total_repeat = 10000
door = [0,0,1]

for i in range(1, total_repeat+1):
    shuffle(door)
    user_choice = choice(door)
