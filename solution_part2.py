"""Advent of Code 2024 - Day 2 - Part 2"""

from solution_part1 import is_safe_report, read_reports


def is_safe_with_dampener(levels: list[int]) -> bool:
    if is_safe_report(levels):
        return True

    for index in range(len(levels)):
        dampened_levels = levels[:index] + levels[index + 1 :]
        if is_safe_report(dampened_levels):
            return True

    return False


def count_safe_reports_with_dampener(reports: list[list[int]]) -> int:
    return sum(is_safe_with_dampener(report) for report in reports)


def main() -> None:
    reports = read_reports("input.txt")
    print(count_safe_reports_with_dampener(reports))


if __name__ == "__main__":
    main()
