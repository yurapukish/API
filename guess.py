# Це гра по відгадуванню чиcел.
from random import randint

# COUNT USERS ATTEMPT

number = randint(1,100)
print("Я загадаю число від 1 до 100. Існує теорія, що Ви гарантовано повинні вгадати число за 7 спроб. Я даватиму Вам підказки. \n Давайте перевіримо її.")
print("Введіть Вашe ім'я: \n")

name = input()
print("Привіт", name, "я загадав число від 1 до 100. Попробуй його відгадати у тебе 7 спроб.")
for attemp in range(1,8):
    print("Спроба №", attemp)
    user_number = int(input("Введіть Вашe число :\n"))
    while user_number > 100:
        print(user_number, "> 1000 . Введіть число від 1 до 100")
        user_number = int(input())
    #user_number = int(user_number)
    if user_number > number:
        print("Твоє число більше за загадане")
    elif user_number < number:
        print("Твоє число менше за загадане")
    else:
        break
if user_number == number:
    print("Вітаю, ", name, "! Ви справилися з завданням з ", attemp, "спроби." )
else:
    print("Жаль, Ви не вгадали. Загадане число було :", number, ".")