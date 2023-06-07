def print_menu():
    print("-------------| 100 спичек |-------------")
    print("1. Описание игры")
    print("2. Игра")
    print("3. Выход")

def get_user_choice():
    return int(input())

def handle_user_choice(choice):
    if choice == 1:
        print_description()
    elif choice == 2:
        play_game()
    elif choice == 3:
        return False
    else:
        print("Выберите корректный пункт меню")
    return True
