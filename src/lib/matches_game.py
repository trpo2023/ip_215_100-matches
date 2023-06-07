def printDescription():
    print(
        "Из кучки, первоначально содержащей 100 спичек, два игрока поочередно берут по несколько спичек: не менее одной и не более десяти.")
    print("Выигрывает тот, кто берет последнюю спичку.")
    print("\nДля возврата в меню нажмите любую клавишу...")
    input()


def changePlayer(playerNumber):
    return 2 if playerNumber == 1 else 1


def isInputCorrect(diff):
    return diff >= 1 and diff <= 10


def playGame():
    matchCount = 100
    player = 1
    print("Начальное количество спичек:", matchCount)

    while matchCount > 0:
        print("\nИгрок", player, "выбирает спички:")
        diff = int(input())

        if not isInputCorrect(diff):
            print("Необходимо выбрать количество спичек в диапазоне от 1 до 10")
        else:
            matchCount -= diff
            print("Количество оставшихся спичек:", matchCount)

            if matchCount <= 0:
                print("Игрок", player, "одержал победу!")

            player = changePlayer(player)

    input()

