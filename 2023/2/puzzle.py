INPUT = 'input.txt'
LIMIT = (12, 13, 14) # (R,G,B)


def _parse_game(str):
    """
    return: tuple of colour count (R, G, B)
    """
    game_set = [0, 0, 0]
    for subset in str.split(', '):
        count, colour = subset.split()
        if colour == 'red':
            game_set[0] = int(count)
        elif colour == 'green':
            game_set[1] = int(count)
        else:
            game_set[2] = int(count)
    return tuple(game_set)


def _is_valid_game(game):
    """
    input: list of tuples, e.g. [(1,2,3), (1,3,4)]
    return: True (valid), False (invalid)
    """
    for subset in game:
        if subset[0] > LIMIT[0] or \
           subset[1] > LIMIT[1] or \
           subset[2] > LIMIT[2]:
            return False
    return True


def check_game(game_str):
    set_str = game_str.split('; ')
    game = map(_parse_game, set_str)
    return _is_valid_game(game)


def main():
    with open(INPUT, 'r') as file:
        sum = 0
        for line in file:
            id, game = line.split(': ')
            if check_game(game):
                sum += int(id.split()[1])
        print(sum)


if __name__ == "__main__":
    main()
