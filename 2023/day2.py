from functools import reduce


INPUT = 'input.txt'
LIMIT = (12, 13, 14) # (R,G,B)


def _parse_result(str):
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


def _part1(game):
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


def _part2(game):
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


def _parse_game(game_str):
    set_str = game_str.split('; ')
    game = map(_parse_result, set_str)
    return game


def part1():
    with open(INPUT, 'r') as file:
        sum = 0
        for line in file:
            id_str, game_str = line.split(': ')
            game = _parse_game(game_str)
            if _part1(game):
                sum += int(id_str.split()[1])
        print(sum)


def part2():
    with open(INPUT, 'r') as file:
        sum = 0
        for line in file:
            id_str, game_str = line.split(': ')
            game = _parse_game(game_str)
            sum += _part2(game)
        print(sum)


if __name__ == "__main__":
    part1()
    part2()
