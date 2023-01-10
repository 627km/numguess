from random import randint
from time import sleep

username = input("Enter your name > ")
print(username, "Welcome! We start game! Guess number!")

# Generate answer
answer = randint(1, 100)
print(answer)

user_answer = int(input(f"{username}, Guess number (1~100) > "))

print(f"Okay, your choice is {user_answer}")

# Compare answer with user_answer
if user_answer == answer:
    print('***************************')
    sleep(1)
    print('***************************')
    sleep(1)
    print('***************************')
    sleep(1)
    print(f'You got it right!! The answer is {answer}!!')
elif user_answer > answer:
    print(f'Keep going ~, that was too high!')
elif user_answer < answer:
    print(f'Kepp going ~, that was too low!')
