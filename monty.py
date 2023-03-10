from random import shuffle, choice

change_for_success = 0
nochange_for_success = 0
total_repeat = 10000
door = [0,0,1]

for i in range(1, total_repeat+1):
    shuffle(door)
    user_choice = choice(door)
    if user_choice == 1:
        nochange_for_success += 1
    elif user_choice == 0:
        change_for_success += 1
change_percent = change_for_success / total_repeat
nochange_percent = nochange_for_success / total_repeat
print(f'nochange for success percentage = {nochange_percent}')
print(f'change for success percentage = {change_percent}')
