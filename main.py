from intro import print_intro
from take_matches import take_matches
from switch_player import switch_player
from result import print_result
def play_game():
    matches = 100
    current_player = 1

    while matches > 0:
        matches = take_matches(matches, current_player)

        if matches == 0:
            print_result(current_player)
        else:
            current_player = switch_player(current_player)

    print("Игра окончена.")

if __name__ == "__main__":
    print_intro()
    play_game()