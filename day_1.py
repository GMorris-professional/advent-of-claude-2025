#!/usr/bin/env python3
"""
Advent of Claude 2025 - Day 1: Secret Entrance (Safe Dial)

A dial with numbers 0-99. Starting at 50, follow rotation instructions.
- Part 1: Count times dial ends at 0 after a rotation
- Part 2: Count times dial passes through 0 during any click
"""


def solve(input_str: str) -> tuple[int, int]:
    """
    Solve both parts in a single pass.
    Returns (part1_answer, part2_answer).
    """
    pos = 50
    part1 = 0
    part2 = 0

    for line in input_str.split('\n'):
        if not line or line.isspace():
            continue

        dist = int(line[1:])

        if line[0] == 'L':
            # Count zero passes for part 2 (inlined)
            if pos == 0:
                part2 += dist // 100
            elif dist >= pos:
                part2 += (dist - pos) // 100 + 1
            pos = (pos - dist) % 100
        else:  # R
            # Count zero passes for part 2 (inlined)
            part2 += (pos + dist) // 100 - pos // 100
            pos = (pos + dist) % 100

        # Part 1: count if we ended at 0
        if pos == 0:
            part1 += 1

    return part1, part2


def main():
    import sys

    # Test with the example
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

    p1, p2 = solve(example)
    print(f"Example - Part 1: {p1} (expected 3), Part 2: {p2} (expected 6)")

    # Try to read puzzle input
    puzzle_input = None
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read()
    except FileNotFoundError:
        if not sys.stdin.isatty():
            puzzle_input = sys.stdin.read()

    if puzzle_input and puzzle_input.strip():
        p1, p2 = solve(puzzle_input)
        print(f"Part 1 answer: {p1}")
        print(f"Part 2 answer: {p2}")


if __name__ == '__main__':
    main()
