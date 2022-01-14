player_a=input("Пользователь 1, выбери и введи (камень, бумага или ножницы): ")
import random
computer=['rock', 'paper' , 'scissors']
computer=(random.random())
print("Компьютер выбрал:",computer,)

def Game(p1, p2):
    if p1 == computer:
        print("Вау, у вас ничья!")
    elif p1 == "камень" and computer == "ножницы":
        print("Пользователь 1 выиграл!")
    elif p1 == "камень" and computer == "бумага":
        print("Компьютер выиграл!")
    elif p1 == "бумага" and computer == "камень":
        print("Пользователь 1 выиграл!")
    elif p1 == "бумага" and computer == "ножницы":
        print("Компьютер выиграл!")
    elif p1 == "ножницы" and computer == "камень":
        print("Компьютер выиграл!")
    elif p1 == "ножницы" and computer == "бумага":
        print("Пользователь 1 выиграл!")
Game(player_a, computer)

playAgain = input("Повторить? (Введите Да или Нет): ")

while playAgain == "Да":
    player_a = input("Пользователь 1, выбери и введи (камень, бумага или ножницы): ")
    computer = input("Компьютер выбрал:",computer,)
    Game(player_a, computer)
else:
    print("Спасибо!")
