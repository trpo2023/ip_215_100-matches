def get_valid_input(matches):
    valid_input = False
    while not valid_input:
        try:
            num_matches = int(input("Сколько спичек вы хотите взять? (1-10): "))
            if num_matches >= 1 and num_matches <= 10 and num_matches <= matches:
                valid_input = True
            else:
                print("Некорректный ввод. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    return num_matches
