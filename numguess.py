from random import randint

username = input("Enter your name > ")
print(username, "Welcome! We start game! Guess number!")

# Generate answer
answer = randint(1, 100)
print(answer)

user_answer = int(input(f"{username}, Guess number (1~100) > "))

print(f"Okay, your choice is {user_answer}")
