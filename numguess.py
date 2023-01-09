from random import randint

username = input("Enter your name > ")
print(username, "Welcome! We start game! Guess number!")

# Generate answer
answer = randint(1, 100)
print(answer)

user_answer = int(input("Enter your answer > "))

print(user_answer)
