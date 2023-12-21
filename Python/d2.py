
with open("../Inputs/day2.txt") as file:
    lines = file.read().splitlines()


def part1(puzzle_input):
    POSSIBLE = {"red": 12, "green": 13, "blue": 14}
    possible_games_sum = 0
    for id, game in enumerate(puzzle_input, start=1):
        game = game.split(': ')[1]
        is_possible = True
        for subset in game.split('; '):
            for duo in subset.split(', '):
                n, color = duo.split(' ')
                if int(n) > POSSIBLE[color]:
                    is_possible = False
                    break
        if is_possible:
            possible_games_sum += id
    return possible_games_sum


def part2(puzzle_input):
    power_sum = 0
    for game in puzzle_input:
        game = game.split(': ')[1]
        ball_set = {"red": 0, "green": 0, "blue": 0}
        for subset in game.split('; '):
            for duo in subset.split(', '):
                n, color = duo.split(' ')
                if int(n) > ball_set[color]:
                    ball_set[color] = int(n)

        power_sum += ball_set['red'] * ball_set['blue'] * ball_set['green']
    return power_sum


print(f"Part1: {part1(lines)}")
print(f"Part2: {part2(lines)}")
