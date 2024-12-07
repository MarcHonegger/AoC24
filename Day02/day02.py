def is_report_safe(r):
    if r[0] < r[-1]:
        # (possible) Ascending order
        return all(-3 <= r[i] - r[i + 1] <= -1 for i in range(len(r) - 1))
    else:
        # (possible) Descending order
        return all(1 <= r[i] - r[i + 1] <= 3 for i in range(len(r) - 1))

reports = [[int(character) for character in line.split()] for line in open("Input02.txt", "r").read().splitlines()]
count = 0
for report in reports:
    for i in range(0, len(report)):
        report_without_number = report[:i] + report[i+1:]
        if is_report_safe(report_without_number):
            count += 1
            break
print(count)
