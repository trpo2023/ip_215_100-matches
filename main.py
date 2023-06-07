import menu

while True:
    menu.print_menu()
    user_choice = menu.get_user_choice()
    if not menu.handle_user_choice(user_choice):
        break
