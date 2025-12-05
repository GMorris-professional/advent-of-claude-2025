#!/usr/bin/env python3
"""
Advent of Claude 2025 - Day 5: Count Accessible Paper Rolls

A roll of paper (@) can be accessed by a forklift if there are fewer than 4
rolls of paper in the 8 adjacent positions.
"""

def count_accessible_rolls(grid_str: str) -> int:
    """
    Count the number of paper rolls that can be accessed by forklifts.

    A roll is accessible if it has fewer than 4 adjacent rolls (in the 8
    surrounding positions).
    """
    # Parse the grid
    lines = grid_str.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    accessible_count = 0

    for row in range(rows):
        for col in range(cols):
            # Only check positions with paper rolls
            if grid[row][col] != '@':
                continue

            # Count adjacent paper rolls
            adjacent_rolls = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Check bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == '@':
                        adjacent_rolls += 1

            # Accessible if fewer than 4 adjacent rolls
            if adjacent_rolls < 4:
                accessible_count += 1

    return accessible_count


def visualize_accessible(grid_str: str) -> str:
    """
    Return a visualization of the grid with accessible rolls marked as 'x'.
    """
    lines = grid_str.strip().split('\n')
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    result = [list(line) for line in lines]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '@':
                continue

            adjacent_rolls = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == '@':
                        adjacent_rolls += 1

            if adjacent_rolls < 4:
                result[row][col] = 'x'

    return '\n'.join(''.join(row) for row in result)


if __name__ == '__main__':
    import sys

    # Test with the example from the puzzle
    example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    print("Example grid:")
    print(example)
    print()
    print("Accessible rolls visualization:")
    print(visualize_accessible(example))
    print()
    example_count = count_accessible_rolls(example)
    print(f"Example answer: {example_count} accessible rolls")
    print(f"Expected: 13")
    print()

    # Try to read the actual puzzle input from file or stdin
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
        answer = count_accessible_rolls(puzzle_input)
        print(f"Puzzle answer: {answer} accessible rolls")
    else:
        print("No input.txt found. Provide input via file or stdin:")
        print("  python3 solution.py < input.txt")
        print("  cat input.txt | python3 solution.py")
