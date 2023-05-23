from input import get_valid_input
from player import switch_player
def play_game():
    matches = 100
    current_player = 1

    while matches > 0:
        print("Спичек на столе:", matches)
        print("Ход игрока", current_player)

        num_matches = get_valid_input(matches)

        matches -= num_matches

        if matches == 0:
            print("Игрок", current_player, "взял последнюю спичку и проиграл!")
            print("Поздравляем игрока", 10 - current_player, "с победой!")
        else:
            current_player = switch_player(current_player)
