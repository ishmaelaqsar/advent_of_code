from functools import reduce

INPUT = 'input.txt'


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


def _get_result(game):
    """
    input: list of tuples, e.g. [(1,2,3), (1,3,4)]
    return: Power
    """
    mins = [1, 1, 1]
    for subset in game:
        mins[0] = max(mins[0], subset[0]) if mins[0] else subset[0]
        mins[1] = max(mins[1], subset[1]) if mins[1] else subset[1]
        mins[2] = max(mins[2], subset[2]) if mins[2] else subset[2]
    return reduce(lambda p, x: p * x, mins)


def check_game(game_str):
    set_str = game_str.split('; ')
    game = map(_parse_game, set_str)
    return _get_result(game)


def main():
    with open(INPUT, 'r') as file:
        sum = 0
        for line in file:
            id, game = line.split(': ')
            sum += check_game(game)
        print(sum)


def test(str):
    sum = 0
    for line in str.split('\n'):
        id, game = line.split(': ')
        sum += check_game(game)
    print(sum)

        
if __name__ == "__main__":
    main()
