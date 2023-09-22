# Игра "Камень, ножници, бумага"
from random import randint
from time import sleep
print("Добро пожаловать!")
def game():
    user = input("Что вы будете ставить(1-Камень, 2-Ножници, 3-Бумага)? :")
    if user == '1' or user == '2' or user == '3':
        user = int(user)
        comp = randint(1, 3)
        user_g = None
        comp_g = None

        if user == 1:
            user_g = "Камень"
        elif user == 2:
            user_g = "Ножници"
        else:
            user_g = "Бумага"

        if comp == 1:
            comp_g = "Камень"
        elif comp == 2:
            comp_g = "Ножници"
        else:
            comp_g = "Бумага"

        print(f'У тебя: {user_g}\nУ компютера: {comp_g}')

        if user == comp:
            print("Ничья")
            print('-' * 20)
        if user == 1 and comp == 2:
            print("Победа!")
            print('-' * 20)
        if user == 1 and comp == 3:
            print("Проигрыш!")
            print('-' * 20)
        if user == 2 and comp == 1:
            print("Проигрыш!")
            print('-' * 20)
        if user == 2 and comp == 3:
            print("Победа!")
            print('-' * 20)
        if user == 3 and comp == 1:
            print("Победа!")
            print('-' * 20)
        if user == 3 and comp == 2:
            print("Проигрыш!")
            print('-' * 20)

        otvet = input("Ещё раз(Да-Y, Нет-N)? :")
        if otvet == "Y" or otvet == "y":
            game()
        elif otvet == "N" or otvet == "n":
            print("Тогда до встречи!")
            sleep(1)
        else:
            print("Так и скажи что нет")
            sleep(1)
    else:
        print("Не шути так!")
        game()
game()
