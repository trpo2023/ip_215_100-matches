import random
from logic import inputNum, inputNum2, pcNum


def print_welcome_message():
    print("Добро пожаловать в игру '100 спичек'!")
    print("Правила игры просты: каждый игрок может брать от 1 до 10 спичек.")
    print("Игроки по очереди берут спички, и победителем считается тот, кто заберет последнюю спичку.")
    print("Удачи!")

def inputNum(number):
    if number < 1 or number > 10:
        return 0
    return 1


def inputNum2(number, count):
    if count[0] < number:
        return 0
    else:
        count[0] -= number
    return 1


def pcNum(quantity, count):
    if quantity > count[0]:
        return 0
    count[0] -= quantity
    return 1

def play():
    print_welcome_message()
    random.seed()
    count = [100]
    buf = ''
    input_num = 0
    key = 2
    choice = ''

    while True:
        count[0] = 100
        while count[0] > 0:
            print("Осталось спичек:", count[0])
            buf = input("Сколько спичек хотите взять? ")

            if not buf.isdigit():
                print("Неправильный ввод")
                continue

            input_num = int(buf)

            if inputNum(input_num) == 0:
                print("Введите число от 1 до 10")
                continue

            if inputNum2(input_num, count) == 0:
                print("Введите допустимое значение")
                continue

            print("Осталось спичек:", count[0])
            key = 2

            if count[0] > 0:
                comp_num = random.randint(1, 10)

                if 13 <= count[0] <= 22:
                    comp_num = count[0] - 12

                if 6 <= count[0] <= 11:
                    comp_num = count[0] - 1

                if pcNum(comp_num, count) == 0:
                    comp_num = random.randint(1, count[0])

                    if comp_num == 0:
                        comp_num += 1

                    count[0] -= comp_num

                print("Компьютер взял:", comp_num)
                key = 1

        if key == 1:
            print("Вы победили")
        else:
            print("Вы проиграли")




