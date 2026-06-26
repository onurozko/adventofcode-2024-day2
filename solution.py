"""Advent of Code 2024 - Day 2"""

def read_reports(path: str) -> list[list[int]]:
    with open(path, encoding="utf-8") as file:
        return [
            [int(level) for level in line.split()]
            for line in file
            if line.strip()
        ]


def is_safe_report(levels: list[int]) -> bool:
    adjacent_differences = [
        levels[index + 1] - levels[index]
        for index in range(len(levels) - 1)
    ]

    increasing = all(1 <= diff <= 3 for diff in adjacent_differences)
    decreasing = all(-3 <= diff <= -1 for diff in adjacent_differences)

    return increasing or decreasing


def count_safe_reports(reports: list[list[int]]) -> int:
    return sum(is_safe_report(report) for report in reports)


def main() -> None:
    reports = read_reports("input.txt")
    print(count_safe_reports(reports))


if __name__ == "__main__":
    main()
