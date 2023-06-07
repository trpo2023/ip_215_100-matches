def print_description():
    print("Из кучки, первоначально содержащей 100 спичек, два игрока поочередно берут по несколько спичек:")
    print("не менее одной и не более десяти.")
    print("Выигрывает тот, кто берет последнюю спичку.")
    input("\nДля возврата в меню нажмите любую клавишу...")

def change_player(player_number):
    return 2 if player_number == 1 else 1

def is_input_correct(diff):
    return 1 <= diff <= 10

def play_game():
    match_count = 100
    player = 1
    print("Начальное количество спичек:", match_count)

    while match_count > 0:
        print("\nИгрок", player, "выбирает спички:")
        diff = int(input())

        if not is_input_correct(diff):
            print("Необходимо выбрать количество спичек в диапазоне от 1 до 10")
        else:
            match_count -= diff
            print("Количество оставшихся спичек:", match_count)

            if match_count <= 0:
                print("Игрок", player, "одержал победу!")

            player = change_player(player)
