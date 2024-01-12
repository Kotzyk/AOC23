import re

with open("../Inputs/day5.txt") as file:
    puzzle_input = file.read()


def part1(puzzle_input):
    segments = puzzle_input.split('\n\n')
    seeds = list(map(int, segments[0].split(': ')[1].split(' ')))
    min_location = float('inf')
    for seed_or_somethingelse in seeds:
        for segment in segments[1:]:
            for value in re.findall(r'(\d+) (\d+) (\d+)', segment):
                destination, start, delta = map(int, value)
                if seed_or_somethingelse in range(start, start + delta):
                    seed_or_somethingelse += destination - start
                    break

        min_location = min(seed_or_somethingelse, min_location)
    return min_location


print('Part 1:', part1(puzzle_input))
# print('Part 2:', part2(puzzle_input))
