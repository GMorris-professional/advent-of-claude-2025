#!/usr/bin/env python3
"""
Advent of Claude 2025 - Day 5: Cafeteria (Fresh Ingredient IDs)

Part 1: Count how many available ingredient IDs are fresh (within any range).
Part 2: Count total unique ingredient IDs considered fresh across all ranges.
"""

def parse_input(data: str) -> tuple[list[tuple[int, int]], list[int]]:
    """
    Parse the database file into ranges and available ingredient IDs.
    Returns (ranges, available_ids).
    """
    parts = data.strip().split('\n\n')

    # Parse ranges
    ranges = []
    for line in parts[0].strip().split('\n'):
        if '-' in line:
            start, end = line.split('-')
            ranges.append((int(start), int(end)))

    # Parse available ingredient IDs (Part 1 only)
    available_ids = []
    if len(parts) > 1:
        for line in parts[1].strip().split('\n'):
            if line.strip():
                available_ids.append(int(line.strip()))

    return ranges, available_ids


def is_fresh(ingredient_id: int, ranges: list[tuple[int, int]]) -> bool:
    """Check if an ingredient ID falls within any fresh range."""
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def count_fresh_available(ranges: list[tuple[int, int]], available_ids: list[int]) -> int:
    """Part 1: Count how many available ingredient IDs are fresh."""
    return sum(1 for id in available_ids if is_fresh(id, ranges))


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping and adjacent ranges."""
    if not ranges:
        return []

    # Sort by start position
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        # Check if overlapping or adjacent (end + 1 >= start means they can merge)
        if start <= last_end + 1:
            # Extend the last range
            merged[-1] = (last_start, max(last_end, end))
        else:
            # Add as a new range
            merged.append((start, end))

    return merged


def count_total_fresh_ids(ranges: list[tuple[int, int]]) -> int:
    """Part 2: Count total unique ingredient IDs considered fresh."""
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        # Range is inclusive, so count is end - start + 1
        total += end - start + 1
    return total


if __name__ == '__main__':
    import sys

    # Test with the example from the puzzle
    example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    ranges, available_ids = parse_input(example)

    print("Example:")
    print(f"  Ranges: {ranges}")
    print(f"  Available IDs: {available_ids}")
    print()

    part1_example = count_fresh_available(ranges, available_ids)
    print(f"  Part 1 (fresh available): {part1_example} (expected: 3)")

    part2_example = count_total_fresh_ids(ranges)
    print(f"  Part 2 (total fresh IDs): {part2_example} (expected: 14)")
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
        ranges, available_ids = parse_input(puzzle_input)

        part1 = count_fresh_available(ranges, available_ids)
        print(f"Part 1 answer: {part1}")

        part2 = count_total_fresh_ids(ranges)
        print(f"Part 2 answer: {part2}")
    else:
        print("No input.txt found. Provide input via file or stdin:")
        print("  python3 day05_cafeteria.py < input.txt")
        print("  cat input.txt | python3 day05_cafeteria.py")
