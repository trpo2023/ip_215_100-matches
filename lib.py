import random


def info(error):
    if error == 'er_not_number':
        print("Это не число!")
        return 1
    elif error == 'er_not_diapazon':
        print("Число не входит в диапазон от 1 до 10!")
        return 2
    elif error == 'er_too_much':
        print("Спичек осталось меньше, чем вы ввели!")
        return 3
    return 0


def winner(kucha, queue):
    if kucha == 0:
        if queue == 1:
            print("\nПобедил игрок!\n\n")
            return 1
        else:
            print("\nПобедил Бот!\n\n")
            return 2
    return 0


def queue(kucha):
    xod_playera(kucha)
    if winner(kucha, 1) == 0:
        xod_bota(kucha)
        winner(kucha, 2)


def xod_bota(kucha):
    print("\nХодит Бот!")
    print("Осталось спичек:", kucha)
    if kucha <= 10:
        bot = kucha
    else:
        bot = random.randint(1, 10)
    print("Он взял:", bot)
    kucha -= bot
    return 0


def digit_or_not(xod):
    if not xod.isdigit():
        return 1
    return 0


def check_diapazon(xod):
    if 1 <= xod <= 10:
        return 0
    return 1


def check_kol_vo(xod, kucha):
    if kucha >= xod:
        kucha -= xod
        return 0
    return 1


def checks(kucha, xod):
    if digit_or_not(xod) != 0:
        info('er_not_number')
        return 1
    player = int(xod)
    if check_diapazon(player) == 1:
        info('er_not_diapazon')
        return 2
    if check_kol_vo(player, kucha) == 1:
        info('er_too_much')
        return 3
    return 0


def xod_playera(kucha):
    xod = input("\nВаш ход!\nОсталось спичек: " + str(kucha) + "\nСколько спичек вы берете: ")
    if xod == "":
        xod = input()
    if checks(kucha, xod) != 0:
        xod_playera(kucha)
    return 0


def start():
    quit = input("Начинаем игру?\n1 - Да; 2 - Нет;\n")
    while True:
        if quit == '2':
            return 1
        elif quit == '1':
            kucha = 100
            while kucha > 0:
                queue(kucha)
            quit = input("Начинаем игру?\n1 - Да; 2 - Нет;\n")
        else:
            print("Нет такого выбора!\nВаше действие: ")
            quit = input()
    return 0


start()
