from random import randint

username = input("Enter your name > ")
print(username, "님 안녕하세요! 지금부터 추측게임을 시작할게요!")

# Generate answer
answer = randint(1, 100)
print(answer)
