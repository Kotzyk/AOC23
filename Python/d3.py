import re

NUMBERS_REGEX: str = r'\d+'

with open("../Inputs/day3.txt") as file:
    lines: list[str] = file.read().splitlines()


def part1(puzzle_input) -> int:
    SYMBOL_REGEX: str = r'[^\.\d]'
    symbol_adjecent_set: set = set()
    for i, line in enumerate(input):
        for m in re.finditer(SYMBOL_REGEX, line):
            j = m.start()
            symbol_adjecent_set |= {(row, col) for row in range(i-1, i+2)
                                    for col in range(j-1, j+2)}
    part_number_sum: int = 0
    for i, line in enumerate(puzzle_input):
        for m in re.finditer(NUMBERS_REGEX, line):
            if any((i, j) in symbol_adjecent_set for j in range(*m.span())):
                part_number_sum += int(m.group())

    return part_number_sum


# def part2(puzzle_input: list[str]) -> int:
#    GEAR_REGEX = r'\*'
#    gear_adjacent_set = adjecent_chars(puzzle_input, GEAR_REGEX)
#    gear_ratio = 1 
#    gears = dict()
#    for i, line in enumerate(puzzle_input):
#        for m in re.finditer(NUMBERS_REGEX, line):
#            if any((i, j) in symbol_adjecent_set for j in range(*m.span())):
#                part_number_sum += int(m.group())
#    return gear_adjacent_set


print(part1(lines))
# print(part2(lines))
