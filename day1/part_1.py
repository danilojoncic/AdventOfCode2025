def solve() -> int:
    dial = 50
    counter = 0

    with open('path/to/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == 'R':
                dial += int(line[1:])
            elif line[0] == 'L':
                dial -= int(line[1:])
            dial = dial % 100
            if dial == 0:
                counter += 1

    return counter


if __name__ == '__main__':
    solution = solve()
    print(solution)

