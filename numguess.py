from random import randint
from time import sleep

username = input("Enter your name > ")
print(username, "Welcome! We start game! Guess number!")
chance = 5
# Generate answer       
answer = randint(1, 100)
print(answer)


# Compare answer with user_answer
for i in range(1,chance+1):
    user_answer = int(input(f"{username}, Guess number (1~100) > "))
    print(f"Okay, your choice is {user_answer}")
    if user_answer == answer:
        print('***************************')
        sleep(1)
        print('***************************')
        sleep(1)
        print('***************************')
        sleep(1)
        print(f'You got it right!! The answer is {answer}!!')
        break
    elif user_answer > answer:
        print(f'Keep going ~, that was too high!')
        print(f'remain chance : {chance - i}')

    elif user_answer < answer:
        print(f'Kepp going ~, that was too low!')
        print(f'remain chance : {chance - i}')