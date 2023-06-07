from matches_game import printDescription, playGame

while True:
    print("\n-------------| 100 спичек |-------------")
    print("1. Описание игры")
    print("2. Игра")
    print("3. Выход")
    selectedOption = int(input())

    if selectedOption == 1:
        printDescription()
    elif selectedOption == 2:
        playGame()
    elif selectedOption == 3:
        break
    else:
        print("Выберите корректный пункт меню")
