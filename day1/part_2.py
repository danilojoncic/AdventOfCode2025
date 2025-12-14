def solve() -> int:
    dial = 50
    counter = 0

    with open('/path/to/input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == 'R':
                for i in range(int(line[1:])):
                    dial += 1
                    if dial % 100 == 0:
                        counter += 1

            elif line[0] == 'L':
                for i in range(int(line[1:])):
                    dial -= 1
                    if dial % 100 == 0:
                        counter += 1

    return counter

if __name__ == '__main__':
    solution = solve()
    print(solution)

