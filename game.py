from random import randint
number = randint(0, 100)
print("*****Отгадайте число от 1 до 100*****")
while True:
    answer = input("Введите число: ")

    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Введите число правильно!")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Загаданное число меньше!")
        continue
    elif user_answer < number:
        print("Загаданное число больше!")
        continue
    else:
        print("Верно!")
        break
