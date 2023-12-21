def read_file_lines(filename):
    with open(filename, 'r') as file:
        lines: list[str] = file.read().splitlines()
    return lines


lines = read_file_lines("../Inputs/day4.txt")


def calculate_numof_matches(card) -> int:
    # parsed card ID is unimportant at this point
    card = card.split(': ')[1]
    winning_nums, current_nums = card.split(' | ')

    # clean double whitespaces
    winning_nums = ",".join(winning_nums.split())
    current_nums = ",".join(current_nums.split())

    # parse to int
    winning_nums = set([eval(n) for n in winning_nums.split(',')])
    current_nums = set([eval(n) for n in current_nums.split(',')])
    matches = len(current_nums.intersection(winning_nums))
    return matches


def part1(puzzle_input) -> int:
    score_total = 0
    for card in puzzle_input:
        matches = calculate_numof_matches(card)
        card_score = 2**(matches-1)
        if card_score >= 1:
            score_total += card_score
    return score_total


def part2(puzzle_input) -> int:
    copies = [1] * len(puzzle_input)
    for id, card in enumerate(puzzle_input, start=0):
        counter = copies[id]
        matches = calculate_numof_matches(card)
        for card_id in range(id+1, id+matches+1):
            copies[card_id] += counter
    return sum(copies)


print(f"Part1: {part1(lines)}")
print(f"Part2: {part2(lines)}")
