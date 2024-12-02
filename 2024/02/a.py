def is_report(report):
    return (
        all(v1 > v2 and v1 - v2 <= 3 for v1, v2 in zip(report, report[1:])) or
        all(v1 < v2 and v2 - v1 <= 3 for v1, v2 in zip(report, report[1:]))
    )


with open('input.txt') as f:
    reports = [[*map(int, line.split())] for line in f]


print(sum(is_report(r) for r in reports))
