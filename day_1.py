#!/usr/bin/env python3
"""
Advent of Claude 2025 - Day 1: Secret Entrance (Safe Dial)

A dial with numbers 0-99. Starting at 50, follow rotation instructions.
- Part 1: Count times dial ends at 0 after a rotation
- Part 2: Count times dial passes through 0 during any click
"""


def parse_rotations(input_str: str) -> list[tuple[str, int]]:
    """Parse rotation instructions into (direction, distance) tuples."""
    rotations = []
    for line in input_str.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        rotations.append((direction, distance))
    return rotations


def solve_part1(rotations: list[tuple[str, int]]) -> int:
    """
    Count how many times the dial ends at 0 after a rotation.
    """
    position = 50
    zero_count = 0

    for direction, distance in rotations:
        if direction == 'L':
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def count_zero_passes_right(position: int, distance: int) -> int:
    """
    Count how many times we pass through 0 when moving right by distance clicks.
    Moving right: position increases, wrapping from 99 to 0.
    """
    # We visit positions position+1, position+2, ..., position+distance (mod 100)
    # We hit 0 when (position + k) % 100 == 0 for k in [1, distance]
    return (position + distance) // 100 - position // 100


def count_zero_passes_left(position: int, distance: int) -> int:
    """
    Count how many times we pass through 0 when moving left by distance clicks.
    Moving left: position decreases, wrapping from 0 to 99.
    """
    # We visit positions position-1, position-2, ..., position-distance (mod 100)
    # We hit 0 when (position - k) % 100 == 0 for k in [1, distance]
    # This means k = position, position+100, position+200, ...
    if position == 0:
        # From 0, we go to 99, 98, ... We only hit 0 again every 100 clicks
        return distance // 100
    else:
        # First hit at k = position, then every 100 clicks after
        if distance < position:
            return 0
        else:
            return (distance - position) // 100 + 1


def solve_part2(rotations: list[tuple[str, int]]) -> int:
    """
    Count how many times any click causes the dial to point at 0.
    This includes passing through 0 during rotations.
    """
    position = 50
    zero_count = 0

    for direction, distance in rotations:
        if direction == 'L':
            zero_count += count_zero_passes_left(position, distance)
            position = (position - distance) % 100
        else:  # R
            zero_count += count_zero_passes_right(position, distance)
            position = (position + distance) % 100

    return zero_count


def main():
    import sys

    # Test with the example from the puzzle
    example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    rotations = parse_rotations(example)

    print("Example rotations:")
    print(example)
    print()

    part1_example = solve_part1(rotations)
    print(f"Part 1 (example): {part1_example}")
    print(f"Expected: 3")
    print()

    part2_example = solve_part2(rotations)
    print(f"Part 2 (example): {part2_example}")
    print(f"Expected: 6")
    print()

    # Try to read the actual puzzle input
    puzzle_input = None

    # First try to read from input.txt
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read()
    except FileNotFoundError:
        pass

    # If no file, check if stdin has data
    if puzzle_input is None and not sys.stdin.isatty():
        puzzle_input = sys.stdin.read()

    if puzzle_input and puzzle_input.strip():
        rotations = parse_rotations(puzzle_input)
        part1 = solve_part1(rotations)
        part2 = solve_part2(rotations)
        print(f"Part 1 answer: {part1}")
        print(f"Part 2 answer: {part2}")
    else:
        print("No input.txt found. Provide input via file or stdin:")
        print("  python3 day_1.py < input.txt")
        print("  cat input.txt | python3 day_1.py")


if __name__ == '__main__':
    main()
