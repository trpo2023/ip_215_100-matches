def changePlayer(player):
    player[0] = 2 if player[0] == 1 else 1


def isInputCorrect(diff):
    return diff[0] in [1, 5, 10]


def test_CHECK_PLAYER_CHANGE():
    player = [1]
    expected = 2
    changePlayer(player)
    assert player[0] == expected

    player[0] = 2
    expected = 1
    changePlayer(player)
    assert player[0] == expected


def test_CHECK_USER_INPUT():
    diff = [100]
    real = isInputCorrect(diff)
    assert not real

    diff[0] = 0
    real = isInputCorrect(diff)
    assert not real

    diff[0] = 1
    real = isInputCorrect(diff)
    assert real

    diff[0] = 5
    real = isInputCorrect(diff)
    assert real

    diff[0] = 10
    real = isInputCorrect(diff)
    assert real

